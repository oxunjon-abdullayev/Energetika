from aiogram import types
from aiogram.dispatcher.filters import Text
from aiogram.types import ReplyKeyboardRemove

from keyboards.default.default_citizen_button import  ortga_qaytish
from keyboards.inline.inline_citizen_button import inline_user_button, show_users, delete_user_button
from loader import dp
from states.citizen_state import DeleteUserState, ShowAllUserState



@dp.message_handler(Text(equals="👥 Fuqarolar"))
async def get_info(message: types.Message):
    await message.answer(text="Fuqarolarni tahrirlash",
                         reply_markup=ReplyKeyboardRemove())
    await message.answer_photo(photo="https://www.atf.gov/sites/default/files/media/2015/08/people.jpg",
                         reply_markup=inline_user_button(),protect_content=True,
                               allow_sending_without_reply=True)


@dp.callback_query_handler()
async def user_callback(callback: types.CallbackQuery):

    if callback.data == "delete_user":
        await callback.message.answer(text="Fuqaroni o'chirish",
                                 reply_markup=ReplyKeyboardRemove())

        await callback.message.answer(text="<b>👥 Ro'yxatda mavjud foydalanuvchilar </b>",

                                      reply_markup=delete_user_button())
        await callback.message.answer(text=f"<b><i>👤 Qaysi id ga tegishli "
                                      "fuqaroni o'chirmoqchisiz ❓\n\n🆔 raqamni kiriting :</i></b>",
                                      reply_markup=ortga_qaytish())
        await DeleteUserState.id.set()

    elif callback.data == "all_user":
        await callback.message.answer(text="<b>Ro'yxatdan o'tgan foydalanuvchilar</b>",
                                      reply_markup=show_users())
        await ShowAllUserState.id.set()
    elif callback.data == 'cancel':
        await callback.message.answer_photo(photo="https://www.atf.gov/sites/default/files/media/2015/08/people.jpg",
                                            reply_markup=inline_user_button())





