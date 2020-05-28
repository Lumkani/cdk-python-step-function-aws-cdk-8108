from aws_cdk import core
import aws_cdk.aws_stepfunctions as sfn
import aws_cdk.aws_stepfunctions_tasks as tasks


class HelloCdkPythonStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        dynamo_put_task = sfn.Task(self, "PutItem",
            task=tasks.CallDynamoDB.put_item(item={'SOME_KEY': tasks.DynamoAttributeValue().with_s('1234')},
                table_name="my-table"))
        task = sfn.Task(self, 'invoke-notification-service', task=dynamo_put_task)
        sfn.StateMachine(self, 'save-event', definition=task)

        # let dynamoPutItem = sfn_tasks.CallDynamoDB.putItem({  #     item: {SOME_KEY: new  #   #  #
        # sfn_tasks.DynamoAttributeValue().withS('1234')},  #     tableName: TABLE_NAME,  #     conditionExpression:
        # 'ForumName <> :f and Subject <> :s',  #     expressionAttributeNames: {OTHER_KEY: '#OK'},
        #     expressionAttributeValues: {  #         ':val': new sfn_tasks.DynamoAttributeValue().withN(  #  #  #
        #     sfn.Data.stringAt('$.Item.TotalCount.N'),  #         ),  #     },  #     returnConsumedCapacity:  #  #
        #     sfn_tasks.DynamoConsumedCapacity.TOTAL,  #     returnItemCollectionMetrics:  #       #  #
        #     sfn_tasks.DynamoItemCollectionMetrics.SIZE,  #     returnValues: sfn_tasks.DynamoReturnValues.ALL_NEW,
        # });
