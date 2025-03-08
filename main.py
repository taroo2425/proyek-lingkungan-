import discord


intents = discord.Intents.default()
intents.message_content = True

#bot = commands.Bot(command_prefix='$', intents=intents)
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'kita sudah masuk sebagai {client.user}')


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith('Hai!'):
        await message.channel.send(f'halo aku adalah {client.user}!')

    elif  message.content.startswith('$heh'):
        if len(message.content) > 4:
            count_heh = int(message.content[4:])
        else:
            count_heh = 5
        await message.channel.send("he" * count_heh)

    elif message.content.startswith('hai aku mau nanya nih!'):
        await message.channel.send("Haii jugaa! mau nanya apaa tuh?")

    elif message.content.startswith('aku mau bertanya'):
        await message.channel.send("iya silahkan bertanya...")

    elif message.content.startswith('apa itu perubahan iklim?'):
        await message.channel.send("Perubahan iklim mengacu pada perubahan jangka panjang dalam suhu rata-rata dan pola cuaca di bumi, biasanya disebabkan oleh perilaku manusia, seperti akibat penggunaan bahan bakar fosil yang meningkatkan emisi gas rumah kaca. Perubahan iklim dapat menyebabkan fenomena ekstrem seperti kenaikan permukaan laut, cuaca yang lebih ekstrim (panas, dingin, kering), dan penurunan keanekaragaman hayati.")
    elif message.content.startswith('apa itu plastik?'):
        await message.channel.send("Plastik adalah salah satu makromolekul yang proses pembentukannya melalui tahap polimerisasi. Polimerisasi adalah suatu proses penggabungan dari beberapa molekul sederhana atau monomer menjadi molekul besar yang disebut makromolekul atau polimer melalui suatu proses kimia.")
    elif message.content.startswith('cara memilah sampah'):
        await message.channel.send("1. Bedakan tempat sampah sesuai kategori agar sampah dapat didaur ulang atau digunakan kembali.    2. Kurangi penggunaan barang yang akan menjadi sampah yang tidak bisa didaur-ulang.     3. Ikut sertakan anak sejak dini untuk meningkatkan pemahaman mengenai pentingnya memilah sampah.")
    elif message.content.startswith('apa saja jenis sampah?'):
        await message.channel.send("macam macam sampah, klasifikasi perbedaan dan karakteristik dari setiap jenis sampah yang ada. Tidak hanya terdiri dari sampah organik dan anorganik, sampah juga dapat dibedakan berdasarkan kategori tertentu. Berikut adalah uraian macam-macam sampah berdasarkan sifat, sumber, dan waktunya.")
    elif message.content.startswith('apa itu sampah organik?'):
        await message.channel.send("Sampah organik merupakan sampah yang berasal dari sisa-sisa makhluk hidup, baik hewan, tanaman, maupun manusia yang dapat terurai secara alamiah di alam (biodegradable). Biasanya sampah jenis ini biasa kita kenal dengan sampah sisa makanan, potongan buah dan sayur, sampah dedaunan, pepohonan, dan rumput-rumputan, sekam padi, kotoran hewan ternak, juga potongan kuku dan helai rambut yang terbuang ke tanah. Sampah organik bisa dibedakan lagi secara lebih mendetail ke dalam dua jenis, yaitu sampah organik kering dan sampah organik basah. Sampah organik kering punya kandungan air yang lebih sedikit dibandingkan sampah organik basah. Oleh karena itu, biasanya sampah organik basah akan lebih cepat membusuk sehingga hancur lebih dulu.")
    elif message.content.startswith('apa itu sampah anorganik?'):
        await message.channel.send("Berbeda dari sampah organik, sampah anorganik tidak dapat terurai secara alami (undegradable) karena materialnya tidak berasal dari alam melainkan hasil olahan dari bahan sintetik tertentu. Beberapa contoh sampah anorganik yang sering dijumpai sehari-hari misalnya seperti kantong plastik, kaleng, aluminium, botol kaca, styrofoam, karton, tekstil dan masih banyak lagi. Barang-barang dengan material tersebut tidak dapat membusuk dengan bantuan alam, untuk itu harus diolah kembali oleh manusia atau mesin agar bisa dimanfaatkan menjadi produk baru.")
    elif message.content.startswith('cara mencegah pencemaran lingkungan?'):
        await message.channel.send("Ada banyak cara yang dapat dilakukan untuk melawan pencemaran lingkungan:    1. Mengurangi konsumsi barang dengan pengadaan bahan baku ramah lingkungan.    2. Meningkatkan kesadaran akan pentingnya kebersihan lingkungan melalui kampanye atau pendidikan.    3. Mengurangi pembakaran bahan bakar fosil untuk pemberdayaan tenaga listrik dengan energi terbarukan.    4. Melindungi lahan basah dan daerah alami untuk meningkatkan penyediaan sumber daya alam.")
    elif message.content.startswith('cara mengurangi sampah'):
        await message.channel.send("Untuk mengurangi sampah, beberapa cara yang bisa dilakukan adalah:   1. Menurunkan konsumsi barang dengan pengadaan yang berkelanjutan.   2. Memulai program daur ulang untuk barang-barang yang bisa didaur ulang.   3. Memulai program kompos dengan menghidupkan kembali barang-barang organik seperti daging dan sayuran.    4. Menurunkan konsumsi plastik dengan mengganti dengan bahan baku yang mudah terurai.")
    elif message.content.startwith('cara menjaga lingkungan agar lebih sehat'):
        await message.channel.send("Ada beberapa cara untuk menjaga lingkungan agar lebih sehat, seperti:     1. Mengurangi konsumsi energi secara berkala melalui pemanfaatan tenaga terbarukan.     2. Memulai program daur ulang dengan mendaurulang sumber daya.     3. Memulai program kompos dengan bahan organik untuk meningkatkan nutrisi tanah.     4. Mengurangi konsumsi barang dengan bahan baku tidak alami.")
    #lanjutt

#@client.event
#async def on_message(message):
#    if message.content.startswith('check'):
#        for attachments in message.channel.send:
#            file_name = attachments.filename
#            file_url = attachments.url
#            await attachments.save(f"./{attachments.filename}")
#            await message.channel.send(get_class(model_path="keras_model.h5", labels_path="labels.txt", image_path=f"./{attachments.filename}"))
#    else:
#        await message.channel.send("belum aploud gambar yak? >:(")
    

client.run("MTM0NTMzODc5NjY0NzkwNzQwMg.GZs_g1.y10UEh6AI2niJEnBSQ8hi6xovm8_gbBEHUUH6Q")