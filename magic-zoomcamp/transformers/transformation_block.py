if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(data, *args, **kwargs):
    """
    Template code for a transformer block.

    Add more parameters to this function if this block has multiple parent blocks.
    There should be one parameter for each output variable from each parent block.

    Args:
        data: The output from the upstream parent block
        args: The output from any additional upstream blocks (if applicable)

    Returns:
        Anything (e.g. data frame, dictionary, array, int, str, etc.)
    """

    data = data.query("passenger_count > 0 and trip_distance > 0")

    # Question 2
    print("Question 2: ", len(data))

    # Question 3
    data['lpep_pickup_date'] = data['lpep_pickup_datetime'].dt.date

    # Question 4
    print("Question 4: ", set(data['VendorID']))

    # Question 5
    column_names = {
        "VendorID": "vendor_id",
        "RatecodeID": "rate_code_id",
        "PULocationID": "pu_location_id",
        "DOLocationID": "do_location_id",
    }

    data.rename(columns=column_names, inplace=True)

    return data


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    
    assert output['vendor_id'].isin([1, 2]).all(), 'Unexpected values in the column vendor_id'

    assert not (output['passenger_count'] == 0).any(), 'There is a ride with no passengers.'

    assert not (output['trip_distance'] == 0).any(), 'There is a ride with no distance.'
