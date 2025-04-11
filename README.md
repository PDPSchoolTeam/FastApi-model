# PDP School API LMS

Bu FastAPI asosidagi API, maktab uchun ta'lim boshqaruv tizimi (LMS). Bu API, maktablar va o'quvchilarni boshqarish uchun nuqta nuqtalarini taqdim etadi, shu jumladan yangi yozuvlar yaratish va ismga asoslangan ma'lumotlarni olish.

## Xususiyatlar

- **Barcha maktablarni olish**: Baza ichidagi barcha maktablarni ko'rsatish.
- **Yangi maktab yaratish**: Maktabni nomi, xonasi va o'qituvchisi bilan qo'shish.
- **Maktabni nomi bo'yicha olish**: Maxsus maktabni nomiga qarab olish.
- **Barcha o'quvchilarni olish**: Baza ichidagi barcha o'quvchilarni ko'rsatish.
- **Yangi o'quvchi yaratish**: Yangi o'quvchi qo'shish, ism, email, xona va o'qishga qabul qilingan sana bilan.
- **O'quvchini nomi bo'yicha olish**: Maxsus o'quvchini ismi bilan olish.

## O'rnatish

Ushbu loyihani lokalda ishga tushirish uchun:

1. Repozitoriyani klonlash:
   ```bash
   git clone https://github.com/PDPSchoolTeam/FastApi-model.git
   cd school-api
   ```
2. Virtual muhit yaratish:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # Windows uchun: `venv\Scripts\activate`
   ```
3. Bog'liqliklarni o'rnatish:
   ```bash
   pip install -r requirements.txt
   ```
