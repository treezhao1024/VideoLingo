from openai import OpenAI
import json_repair
api_set = {
    "model": "qwen2.5:32b",
    "base_url": "http://127.0.0.1:11434",

}

base_url = api_set["base_url"].strip('/') + '/v1' if 'v1' not in api_set["base_url"] else api_set["base_url"]
client = OpenAI(api_key='st-1234', base_url=base_url)
response_format = {"type": "json_object"}
# if response_json and api_set["model"] in llm_support_json else None

prompt = """
### Role
You are a video translation expert and terminology consultant, specializing in en comprehension and 简体中文 expression optimization.

### Task
For the provided en video text:
1. Summarize main topic in two sentences
2. Extract professional terms/names with 简体中文 translations
3. Provide brief explanation for each term

### Steps
1. Topic Summary:
   - Quick scan for general understanding
   - Write two sentences: first for main topic, second for key point
2. Term Extraction:
   - Mark professional terms and names
   - Provide 简体中文 translation or keep original
   - Add brief explanation
   - Keep abbreviations and proper nouns unchanged





### Source Text
<text>
I have a confession to make. But first, I want you to make a little confession to me. In the past year I want you to just raise your hand if you've experienced relatively little stress. Anyone? How about a moderate amount of stress? Who's experienced a lot of stress? Yeah, me too. But that is not my confession. My confession is this. I am a health psychologist and my mission is to help people be happier and healthier. But I fear that something I've been teaching for the last 10 years is doing more harm than good and it has to do with stress. For years, I've been telling people stress makes you sick. It increases the risk of everything from the common cold to cardiovascular disease. Basically, I've turned stress into the enemy. But I've changed my mind about stress. And today, I want to change yours. Let me start with the study that made me rethink my whole approach to stress. This study tracked 30,000 adults in the United States for eight years. And they started by asking people how much stress have you experienced in the last year? They also asked, do you believe that stress is harmful for your health? And then they used public death records to find out who died. Okay. Some bad news first. People who experienced a lot of stress in the previous year had a 43% increased risk of dying. that was only true for the people who also believed that stress is harmful for your health. People who experienced a lot of stress but did not view stress as harmful were no more likely to die. In fact, they had the lowest risk of dying of anyone in the study including people who had relatively little stress. Now, the researchers estimated that over the eight years they were tracking deaths 182,000 Americans died prematurely not from stress but from the belief that stress is bad for you. That is over 20,000 deaths a year. Now, if that estimate is correct That would make believing stress is bad for you the 15th largest cause of death in the United States last year, killing more people than skin cancer, HIV, AIDS and homicide. You can see why the study freaked me out. Here I've been spending so much energy telling people stress is bad for your health. So this study got me wondering can changing how you think about stress make you healthier? And here, the science says yes. When you change your mind about stress you can change your body's response to stress. Now, to explain how this works I want you all to pretend that you are participants in a study designed to stress you out. It's called the social stress test. You come into the laboratory and you're told you have to give a five-minute impromptu speech on your personal weaknesses to a panel of expert evaluators sitting right in front of you. And to make sure you feel the pressure there are bright lights and a camera in your face, kind of like this. And the evaluators have been trained to give you discouraging non-verbal feedback, like this. Now that you're sufficiently demoralized, time for part two, a math test. And, unbeknownst to you the experimenter has been trained to harass you during it. Now, we're going to all do this together. It's going to be fun. For me. Okay. I want you all to count backwards from 996 in increments of seven. You're going to do this out loud as fast as you can, starting with 996. Go. Go faster. Faster, please. You're going too slow. Stop, stop, stop, stop. That guy made a mistake. We're going to have to start all over again. You're not very good at this, are you? Okay, so you get the idea. Now, if you were actually in this study you'd probably be a little stressed out. Your heart might be pounding you might be breathing faster, maybe breaking out into a sweat. And normally, we interpret these physical changes as anxiety or signs that we aren't coping very well with the pressure. But what if you viewed them instead as signs that your body was energized was preparing you to meet this challenge? Now, that is exactly what participants were told in a study conducted at Harvard University. Before they went through the social stress test they were taught to rethink their stress response as helpful. That pounding heart is preparing you for action. If you're breathing faster it's no problem. It's getting more oxygen to your brain. And participants who learned to view the stress response as helpful for their performance, well they were less stressed out, less anxious, more confident but the most fascinating finding to me was how their physical stress response changed. Now, in a typical stress response your heart rate goes up and your blood vessels constrict like this. And this is one of the reasons that chronic stress is sometimes associated with cardiovascular disease. It's not really healthy to be in this state all the time. But in the study when participants viewed their stress response as helpful their blood vessels stayed relaxed like this. Their heart was still pounding but this is a much healthier cardiovascular profile. It actually looks a lot like what happens in moments of joy and courage. Over a lifetime of stressful experiences this one biological change could be the difference between a stress-induced heart attack at age 50 and living well into your 90s. And this is really what the new science of stress reveals that how you think about stress matters. So my goal as a health psychologist has changed. I no longer want to get rid of your stress. I want to make you better at stress. And we just did a little intervention. If you raised your hand and said you'd had a lot of stress in the last year we could have saved your life. Because hopefully, the next time your heart is pounding from stress you're going to remember this talk and you're going to think to yourself this is my body helping me rise to this challenge. And when you view stress in that way your body believes you and your stress response becomes healthier. Now, I said I have over a decade of demonizing stress to redeem myself from so we are going to do one more intervention. I want to tell you about one of the most underappreciated aspects of the stress response. And the idea is this stress makes you social. To understand the side of stress we need to talk about a hormone, oxytocin. And I know, oxytocin has already gotten as much hype as a hormone can get. It even has its own cute nickname, the cuddle hormone because it's released when you hug someone. But this is a very small part of what oxytocin is involved in. Oxytocin is a neurohormone. It fine-tunes your brain's social instincts. It primes you to do things that strengthen close relationships. Oxytocin makes you crave physical contact with your friends and family. It enhances your empathy. It even makes you more willing to help and support the people you care about. Some people have even suggested we should snort oxytocin. to become more compassionate and caring. But here's what most people don't understand about oxytocin. It's a stress hormone. Your pituitary gland pumps this stuff out as part of the stress response. It's as much a part of your stress response as the adrenaline that makes your heart pound. And when oxytocin is released in the stress response it is motivating you to seek support. Your biological stress response is nudging you to tell someone how you feel instead of bottling it up. Your stress response wants to make sure you notice when someone else in your life is struggling so that you can support each other. When life is difficult your stress response wants you to be surrounded by people who care about you. Okay, so how is knowing this side of stress going to make you healthier? Well, oxytocin doesn't only act on your brain it also acts on your body. And one of its main roles in your body is to protect your cardiovascular system from the effects of stress. It's a natural anti-inflammatory. It also helps your blood vessels stay relaxed during stress. But my favorite effect on the body is actually on the heart. Your heart has receptors for this hormone. and oxytocin helps heart cells regenerate and heal from any stress-induced damage. This stress hormone strengthens your heart. And the cool thing is that all of these physical benefits of oxytocin are enhanced by social contact and social support. So when you reach out to others under stress either to seek support or to help someone else. You release more of this hormone your stress response becomes healthier and you actually recover faster from stress. I find this amazing that your stress response has a built-in mechanism for stress resilience. And that mechanism is human connection. I want to finish by telling you about one more study. And listen up, because this study could also save a life. This study tracked about 1,000 adults in the United States and they ranged in age from 34 to 93. And they started the study by asking how much stress have you experienced in the last year? They also asked, how much time have you spent helping out friends, neighbors, people in your community? and then they use public records for the next five years to find out who died. Okay, so the bad news first. For every major stressful life experience like financial difficulties or family crisis that increased the risk of dying by 30%. But, and I hope you are expecting a but by now but that wasn't true for everyone. People who spent time caring for others showed absolutely no stress-related increase in dying, zero. Caring created resilience. And so we see once again that the harmful effects of stress on your health are not inevitable. How you think and how you act can transform your experience of stress. When you choose to view your stress response as helpful You create the biology of courage. And when you choose to connect with others under stress you can create resilience. Now, I wouldn't necessarily ask for more stressful experiences in my life but this science has given me a whole new appreciation for stress. Stress gives us access to our hearts. The compassionate heart that finds joy and meaning in connecting with others, and yes your pounding physical heart working so hard to give you strength and energy. And when you choose to view stress in this way you're not just getting better at stress you're actually making a pretty profound statement. You're saying that you can trust yourself to handle life's challenges. And, you're remembering that you don't have to face them alone. Thank you. This is kind of amazing what you're telling us. It seems amazing to me that a belief about stress can make so much difference to someone's life expectancy. How would that extend to advice Like if someone's making a lifestyle choice between, say, a stressful job and a non-stressful job does it matter which way they go that it's equally wise to go for the stressful job so long as you believe that you can handle it in some sense? Yeah, and one thing we know for certain is that chasing meaning is better for your health than trying to avoid discomfort. And so I would say that's really the best way to make decisions is go after what it is that creates meaning in your life and then trust yourself to handle the stress that follows. Thank you so much, Kelly.
</text>

### Output in Json Format
{
    "topic": "Two-sentence video summary",
    "terms": [
        {
            "src": "en term",
            "tgt": "简体中文 translation or original",
            "note": "Brief explanation"
        },
        ...
    ]
}
"""
messages = [{"role": "user", "content": prompt}]


response = client.chat.completions.create(
    model=api_set["model"],
    messages=messages,
    response_format=response_format,
    timeout=150  # ! set timeout
)

print(response.choices[0].message.content)
response_json = True

if response_json:
    try:
        response_data = json_repair.loads(response.choices[0].message.content)
        print(f"the maned response{response_data}")

        # check if the response is valid, otherwise save the log and raise error and retry
        # if valid_def:
        #     valid_response = valid_def(response_data)
        #     if valid_response['status'] != 'success':
        #         save_log(api_set["model"], prompt, response_data, log_title="error", message=valid_response['message'])
        #         raise ValueError(f"❎ API response error: {valid_response['message']}")
        #
        # break  # Successfully accessed and parsed, break the loop
    except Exception as e:
        response_data = response.choices[0].message.content
        print(f"❎ json_repair parsing failed. Retrying: '''{response_data}'''")
        # save_log(api_set["model"], prompt, response_data, log_title="error", message=f"json_repair parsing failed.")
        # if attempt == max_retries - 1:
        #     raise Exception(
        #         f"JSON parsing still failed after {max_retries} attempts: {e}\n Please check your network connection or API key or `output/gpt_log/error.json` to debug.")
else:
    response_data = response.choices[0].message.content
    # break  # Non-JSON format, break the loop directly
print("end")