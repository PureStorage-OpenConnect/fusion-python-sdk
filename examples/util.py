import fusion
import time
import json


def wait_operation_finish(op_id:str, client:fusion.ApiClient) -> fusion.models.operation.Operation:
    """
    wait_operation_finish wait until operation status is Succeeded or Failed. Then returns you that operation.
    if the operation takes longer than expected, it will raise an Exception
    Args:
        op_id (str): the id of operation
        client (fusion.ApiClient): 

    Raises:
        Exception

    Returns:
        fusion.models.operation.Operation
    """
    op_cli = fusion.OperationsApi(client)
    while True:
        op = op_cli.get_operation(op_id)
        if op.status == "Succeeded" or op.status == "Failed":
            return op
        time.sleep(op.retry_in / 1000)

def wait_operation_succeeded(op_id:str, client:fusion.ApiClient) -> fusion.models.operation.Operation:
    """
    wait_operation_succeeded calls wait_operation_finish and expect the result is succeeded.
    if the operation is in other status, it will raise an expection

    Args:
        op_id (str)
        client (fusion.ApiClient)

    Raises:
        Exception

    Returns:
        fusion.models.operation.Operation
    """
    op = wait_operation_finish(op_id, client)
    if op.status == "Succeeded":
        return op
    else:
        # this is how we handle asynchronous error
        # if operation failed, the error field should be set. We can check it by op.error
        # op.error uses fusion.models.error.Error
        print_error(op.error)
        raise Exception(f"operation did not succeed! {op}")

def ApiException_to_ErrorResponse(e: fusion.rest.ApiException) -> fusion.models.error_response.ErrorResponse:
    """
        the current swagger spec only allow the response of most request to be Operation. 
        So when it sees different response body such as ErrorResponse it will raise an ApiException.
        But the body of ApiException still contains all information for ErrorResponse.
        This function is used to convert the ApiException to ErrorResponse.

    Args:
        e (fusion.rest.ApiException)

    Returns:
        fusion.models.error_response.ErrorResponse
    """
    error_response_dict = json.loads(e.body)
    err_dict = error_response_dict['error']
    err = fusion.models.error.Error(**err_dict)
    return fusion.models.error_response.ErrorResponse(request_id=error_response_dict['request_id'], error=err)

error_codes = {"INTERNAL","NOT_FOUND","ALREADY_EXISTS","INVALID_ARGUMENT","NOT_AUTHENTICATED",
                  "PERMISSION_DENIED","NOT_IMPLEMENTED","FAILED_PRECONDITION","CONFLICT","FAILED_TRANSACTION"}

def print_error(err:fusion.models.error.Error):
    """
    this function prints all fields in Error

    Args:
        err (fusion.models.error.Error)
    """
    if err is None:
        return
    if err.pure_code in error_codes:
        pass
    else:
        print("unknown pure code")
    print(f"pure_code={err.pure_code}; http_code={err.http_code}; message={err.message}; details={err.details}")
