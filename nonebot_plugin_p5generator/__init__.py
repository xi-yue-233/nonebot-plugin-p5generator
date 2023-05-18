from nonebot import on_command
from nonebot.adapters.onebot.v11 import Message, MessageSegment
from nonebot.params import CommandArg

from .generator import generate_image,generate_ui

p5=on_command('p5generator', aliases={'p5预告信'})
p5_ui=on_command('p5ui', aliases={'p5风格'})

@p5.handle()
async def p5generator(args: Message = CommandArg()):
    if not args.extract_plain_text():
        await p5.finish(f"给我要生成的语句啊，不然佐仓双叶来了都没办法生成")
    image = await generate_image(args.extract_plain_text())
    await p5.finish(MessageSegment.image(image))

@p5_ui.handle()
async def p5generatorui(args: Message = CommandArg()):
    if not args.extract_plain_text():
        await p5.finish(f"给我要生成的语句啊，不然佐仓双叶来了都没办法生成")
    image = await generate_ui(args.extract_plain_text())
    await p5.finish(MessageSegment.image(image))
