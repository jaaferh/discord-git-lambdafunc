from discord_webhook.webhook import DiscordEmbed, DiscordWebhook
import json


def lambda_handler(event, context, discord_wh_url):
    # Decipher JSON from Github Webhook
    body = json.loads(event['body'])

    commits = body['commits']    
    repo_name = body['repository']['full_name']
    author = commits[0]['author']['username']
    commit_count = str(len(commits)) + (' commits' if len(commits) > 1 else ' commit')

    commits_title = "%s pushed to %s by %s" % (commit_count, repo_name, author)
    commits_desc = ""
    for commit in commits:
        desc = "`%s`: %s \n" % (commit['id'][:6], commit['message'])
        commits_desc += desc


    # # Create Discord Embedded message and send it through Discord Webhook
    webhook = DiscordWebhook(url=discord_wh_url)

    embed = DiscordEmbed(
        title=commits_title,
        description=commits_desc,
        color="03b2f8"
    )

    webhook.add_embed(embed)
    webhook.execute()    

    print(commits_title)
    print(commits_desc)


    # Assign commit details to a response object and return the object
    response_object = {}
    response_object['statusCode'] = 200

    return response_object

if __name__ == "__main__":
    f = open('event.json',)

    data = json.load(f)
    # data = json.loads()
    lambda_handler(data, None, "https://discord_webhook_url")
