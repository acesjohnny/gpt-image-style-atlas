# Style-card data: (group, name, style description). Each description names the recognizable materials, line, color and texture of the style; the same SUBJECT is rendered in every style for side-by-side comparison.
SUBJECT_EN = ("a seven-year-old child sitting on a cushioned window seat, reading an open picture book, "
              "a small cat curled up asleep beside the child, a potted plant on the windowsill, "
              "soft afternoon light coming through the window")
SUBJECT_ZH = "七岁小孩坐在窗边软垫上读绘本，身边一只小猫蜷着睡觉，窗台一盆绿植，午后阳光照进来"

GROUPS = ["中国传统", "民国与近代", "手绘", "绘画与艺术流派", "版画与印刷", "卡通与动漫", "3D 与手作材质", "摄影与影视", "设计与图解"]

STYLES = [
 # 中国传统
 (0, "工笔重彩", "Chinese gongbi meticulous heavy-color painting on aged silk: fine even ink outlines, flat layered mineral pigments (azurite, malachite, cinnabar), delicate patterned textiles, no Western shading"),
 (0, "水墨写意", "Chinese xieyi freehand ink wash painting on raw xuan paper: expressive loose brushstrokes, ink bleeding and dry-brush texture, mostly black ink with a few pale color washes, generous empty space, a red seal stamp"),
 (0, "白描线稿", "Chinese baimiao pure line drawing: only fine black ink contour lines of varying pressure on off-white paper, no color, no shading, classical figure-painting line quality"),
 (0, "青绿山水", "Chinese blue-green landscape painting style (qinglü): rich azurite blue and malachite green mineral colors, gold outlines, the window framing a miniature blue-green mountain landscape, silk scroll texture"),
 (0, "宋画小品", "Song dynasty album-leaf painting: small round fan-shaped composition, restrained muted colors on aged silk, refined realism, calm poetic atmosphere, soft ink gradations"),
 (0, "界画", "Chinese jiehua ruled-line architectural painting: precise straight ruler-drawn lines of wooden window lattices and beams, isometric-like classical perspective, small detailed figure, ink and light color on silk"),
 (0, "敦煌壁画", "Dunhuang Mogao cave mural painting: earthy ochre, malachite green and faded lapis colors, cracked flaking plaster wall texture, flowing ribbon-like lines, flat decorative halos and floral borders"),
 (0, "木版年画", "Chinese woodblock New Year print (Yangliuxue / Taohuawu nianhua): bold black carved outlines, bright flat pink, red, green and yellow, chubby auspicious child figure, festive decorative border, visible paper grain"),
 (0, "剪纸", "Chinese red paper-cut art: the entire scene cut from a single sheet of red paper, intricate hollow cutout patterns, symmetrical decorative motifs, placed on a plain white background, crisp paper edges"),
 (0, "皮影", "Chinese shadow puppetry (piying): translucent colored leather puppet figures with jointed limbs and perforated patterns, backlit on a glowing warm screen, visible rods holding the figures"),
 (0, "连环画", "Chinese lianhuanhua 1960s-80s picture-story book illustration: fine black pen-and-ink hatching, realistic drawing, printed on slightly yellowed cheap paper, a small caption box at the bottom"),
 (0, "青花瓷纹", "blue-and-white Chinese porcelain painting: the whole scene painted in cobalt blue on glossy white porcelain, curved plate surface, traditional scroll and wave borders, glaze sheen"),
 (0, "苏绣刺绣", "Suzhou silk embroidery: the scene stitched in fine lustrous silk threads, visible stitch direction and thread sheen, subtle color gradients, set in a round embroidery hoop on silk fabric"),
 (0, "篆刻印章", "Chinese seal-carving (zhuanke) art: the scene simplified into a square red seal impression, carved stone-seal lines, red cinnabar ink on white xuan paper, rough chiseled edges"),
 (0, "国潮插画", "modern Chinese guochao trendy illustration: bold flat graphic shapes, traditional cloud and wave patterns, vermilion, jade green and gold palette, clean vector finish with paper texture"),
 # 民国与近代
 (1, "民国月份牌", "1930s Republic of China yuefenpai calendar poster: soft airbrushed rubbed-charcoal-and-watercolor technique, rosy cheeks, pastel colors, decorative Art Deco border with a calendar strip, yellowed aged paper"),
 (1, "老上海广告画", "1930s old Shanghai commercial advertisement poster: hand-painted gouache, bold vintage Chinese lettering headline, Art Deco layout, warm faded reds and teals, printed paper wear"),
 (1, "手工上色老照片", "hand-tinted early 20th century black-and-white photograph: soft sepia base with delicate hand-applied watercolor tints on cheeks and fabrics, film grain, scratches, deckled photo border"),
 (1, "民国书籍装帧", "1930s Chinese book cover design: simple woodcut-like illustration, two-color print (ink black plus one accent), hand-drawn title calligraphy, aged cloth-paper texture"),
 (1, "丰子恺式漫画", "gentle Chinese manhua in the spirit of Feng Zikai: simple warm brush-ink lines, faceless or minimal-featured figures, light pale color washes, lots of white space, a short handwritten Chinese poem line"),
 (1, "五六十年代宣传画", "1950s-60s Chinese poster art style: bright saturated flat colors, strong heroic lighting, smooth painted gouache rendering, optimistic mood, bold printed border"),
 (1, "八十年代挂历", "1980s Chinese wall calendar photo-illustration: slightly soft-focus glamour, saturated warm colors, printed halftone look, month grid at the bottom, glossy paper"),
 (1, "上美厂水墨动画", "Shanghai Animation Film Studio ink-wash animation still (like 'Where Is Mama'): animated frame in pure Chinese ink wash, soft wet edges, no outlines, pale background, cinematic 4:3 frame"),
 (1, "上美厂剪纸动画", "Shanghai Animation Film Studio paper-cut animation still: layered colored paper-cut characters with visible cut edges and joints, flat stage-like background, warm folk colors"),
 (1, "港风电影海报", "1990s Hong Kong movie poster: hand-painted airbrush portrait, dramatic warm lighting, bold Chinese movie-title calligraphy with English subtitle, credits block at the bottom"),
 (1, "老香港招牌街景", "old Hong Kong street illustration: the window view shows dense neon and painted shop signs, tong lau buildings, retro 1970s palette, gouache and ink illustration"),
 # 手绘
 (2, "铅笔素描", "graphite pencil sketch on textured drawing paper: tonal shading with visible hatching, smudged soft areas, loose construction lines, monochrome grey"),
 (2, "炭笔", "charcoal drawing on toned paper: deep rich blacks, dramatic smudged shadows, white chalk highlights, gestural expressive strokes"),
 (2, "彩铅", "colored pencil illustration: soft layered colored pencil strokes with visible paper tooth, gentle pastel palette, hand-drawn warmth"),
 (2, "钢笔淡彩", "pen and ink with light watercolor wash: confident black ink linework, loose transparent watercolor washes spilling outside the lines, white paper showing through"),
 (2, "针管线稿", "fineliner technical pen drawing: clean uniform black lines, stippling and cross-hatching for shadows, detailed line art, no color"),
 (2, "圆珠笔", "blue ballpoint pen drawing on lined notebook paper: dense scribbled hatching, pressure variation, ink blobs, casual doodle energy"),
 (2, "马克笔", "alcohol marker illustration: bold translucent marker strokes with streaky overlaps, crisp outlines, design-sketch look, limited palette"),
 (2, "蜡笔", "wax crayon drawing: waxy textured strokes, bright primary colors, paper texture showing through, charmingly rough"),
 (2, "油画棒", "oil pastel drawing: thick creamy blended strokes, vivid saturated colors, scratched sgraffito details, textured heavy paper"),
 (2, "色粉", "soft pastel drawing on colored paper: powdery blended color, soft edges, velvety light, visible pastel dust texture"),
 (2, "城市速写", "urban sketching style: quick loose ink lines plus fast watercolor splashes, slightly wobbly perspective, handwritten date note in the corner, sketchbook page"),
 (2, "手账涂鸦", "bullet-journal doodle style: cute simple black marker doodles, washi tape, small stickers and hand-lettered notes around the drawing on dotted grid paper"),
 (2, "儿童画", "child's drawing made by a six-year-old: naive wobbly lines, crayon and marker, disproportionate figures, a sun in the corner, joyful imperfect coloring"),
 (2, "黑板粉笔画", "chalkboard chalk art: colorful chalk drawing on a dark green classroom blackboard, dusty smudged texture, hand-lettered chalk title"),
 # 绘画与艺术流派
 (3, "古典油画", "old master oil painting (17th century Dutch style): chiaroscuro window light like Vermeer, rich glazes, fine craquelure, dark warm background"),
 (3, "印象派", "French impressionist oil painting: visible broken brushstrokes, dappled sunlight, soft vibrant color, plein-air feel like Monet or Renoir"),
 (3, "梵高式厚涂", "post-impressionist impasto in the manner of Van Gogh: thick swirling directional brushstrokes, bold complementary blues and yellows, expressive energy"),
 (3, "点彩", "pointillism like Seurat: the whole image built from tiny dots of pure color, optical color mixing, calm luminous atmosphere"),
 (3, "水彩", "transparent watercolor painting: soft wet-on-wet blooms, granulation, preserved white paper highlights, delicate luminous color"),
 (3, "水粉", "gouache painting: opaque matte flat color areas, clean painterly edges, mid-century illustration feel"),
 (3, "丙烯", "acrylic painting: bold opaque colors, confident visible brush marks, contemporary painterly finish on canvas"),
 (3, "中世纪手抄本", "medieval illuminated manuscript page: flat gold leaf, ornate decorated initial letter, vine borders, tempera colors on vellum, gothic script text lines"),
 (3, "浮世绘", "Japanese ukiyo-e woodblock print: bold outlines, flat colors, Prussian blue and soft reds, patterned textiles, paper grain and slight registration offsets"),
 (3, "新艺术慕夏", "Art Nouveau poster in the manner of Alphonse Mucha: flowing organic lines, decorative halo circle, floral ornaments, muted gold and sage palette"),
 (3, "装饰艺术", "Art Deco illustration: geometric streamlined forms, sunburst motifs, gold and black with jewel tones, elegant 1920s glamour"),
 (3, "立体派", "cubist painting: fragmented geometric planes, multiple viewpoints at once, muted browns and blues, Picasso and Braque inspired"),
 (3, "表现主义", "German expressionist painting: distorted forms, raw bold brushstrokes, intense unnatural colors, emotional tension"),
 (3, "超现实主义", "surrealist painting like Magritte and Dalí: the window opens onto a dreamlike sky inside the room, impossible scale, smooth precise rendering"),
 (3, "波普艺术", "pop art like Roy Lichtenstein: Ben-Day dots, thick black outlines, primary colors, comic speech bubble"),
 (3, "野兽派", "fauvism like Matisse: wild non-naturalistic flat colors, simplified shapes, bold decorative patterns"),
 (3, "朴素艺术", "naive folk art like Henri Rousseau: flat perspective, meticulous leaves and plants, childlike sincerity, lush greens"),
 (3, "俄罗斯民间画", "Russian folk art (Palekh lacquer miniature / Khokhloma): black lacquer background, gold filigree, jewel-like tiny painted figures, red and gold ornaments"),
 # 版画与印刷
 (4, "木刻版画", "black-and-white woodcut print: bold carved gouge marks, strong contrast, rough wood grain texture, hand-printed ink imperfections"),
 (4, "铜版蚀刻", "copperplate etching: fine cross-hatched engraved lines, sepia ink, plate tone and plate-mark border, antique book illustration"),
 (4, "丝网印刷", "screen print poster: 3-4 flat spot colors, slight misregistration, bold simplified shapes, halftone gradients"),
 (4, "孔版 Risograph", "risograph print: fluorescent pink and teal spot inks, grainy texture, overprint color mixing, slight misregistration, zine aesthetic"),
 (4, "复古旅行海报", "vintage 1930s travel poster: flat lithographic colors, simplified bold shapes, dramatic perspective, large title lettering at the top"),
 (4, "半调网点", "halftone print style: the image made of enlarged CMYK halftone dots, newspaper-comic texture, limited palette"),
 (4, "蓝晒", "cyanotype print: Prussian blue and white only, photogram look with plant silhouettes, uneven hand-brushed edges on watercolor paper"),
 (4, "橡皮章", "hand-carved rubber stamp print: simple chunky stamped shapes, uneven ink coverage, two ink colors, charming handmade imperfections"),
 (4, "老教科书插图", "1950s children's textbook illustration: simple clear line drawing with two flat printed colors, slightly faded, educational and friendly, printed paper texture"),
 (4, "报纸漫画", "classic newspaper comic strip panel: clean ink lines, flat newsprint colors, dot shading, hand-lettered caption, slightly yellowed newsprint"),
 # 卡通与动漫
 (5, "皮克斯 3D", "Pixar-style 3D animated film still: soft subsurface skin, large expressive eyes, warm global illumination, cinematic depth of field"),
 (5, "迪士尼经典 2D", "classic hand-drawn 2D Disney animation: clean ink-and-paint cels, painted watercolor background, fluid appealing character design"),
 (5, "吉卜力感", "hand-painted Japanese anime film background style reminiscent of Studio Ghibli: lush painted greenery through the window, gentle clouds, warm nostalgic light, simple cel-shaded character"),
 (5, "日式赛璐璐动漫", "modern Japanese TV anime cel shading: crisp outlines, two-tone hard shadows, bright clean colors, anime key visual"),
 (5, "日漫黑白网点", "black-and-white Japanese manga page panel: screentone shading, speed lines, ink hatching, hand-lettered sound effect"),
 (5, "美式卡通", "American TV cartoon style: thick uniform outlines, simple geometric character design, flat bright colors, exaggerated expressions"),
 (5, "美漫", "American comic book art: bold inking, dramatic shadows, dynamic angle, vivid flat coloring, comic panel border"),
 (5, "丁丁清线漫画", "Franco-Belgian ligne claire comic style (the clear-line drawing tradition of Hergé): uniform clean outlines, flat colors without shading, detailed tidy background. Original characters only: the child is an ordinary seven-year-old with dark hair, NOT Tintin, no quiff, no Snowy, no existing comic character"),
 (5, "Q版", "chibi style: big head small body proportions, super-deformed cute characters, pastel colors, sparkles"),
 (5, "绘本插画", "contemporary children's picture book illustration: soft textured gouache and colored pencil, cozy warm palette, whimsical details, gentle storytelling mood"),
 (5, "扁平矢量", "flat vector illustration: geometric shapes, no outlines, limited modern palette, subtle grain, clean editorial look"),
 (5, "儿童教育卡通", "friendly educational cartoon for kids: rounded shapes, bright cheerful colors, clear simple forms, clean white background, easy to read"),
 (5, "贴纸风", "die-cut sticker design: cute bold-outlined characters with a thick white sticker border and a soft drop shadow, glossy finish"),
 (5, "像素 8-bit", "8-bit pixel art: chunky pixels, limited 16-color palette, retro NES game screen look"),
 (5, "90 年代像素游戏", "1990s 16-bit JRPG pixel art scene: detailed pixel tiles, soft dithered lighting, top-down three-quarter view, retro game UI box at the bottom"),
 (5, "涂色本线稿", "coloring book page: clean bold black outlines only, no shading, no fill, large closed areas ready for kids to color, white background"),
 # 3D 与手作材质
 (6, "黏土定格", "claymation stop-motion still: handmade plasticine figures with fingerprints and tool marks, miniature set, soft studio lighting"),
 (6, "羊毛毡", "needle-felted wool figures: fuzzy wool fiber texture, soft rounded forms, miniature handmade diorama, cozy lighting"),
 (6, "钩织玩偶", "crochet amigurumi dolls: visible yarn stitches, soft knitted texture, handmade toy diorama, warm muted colors"),
 (6, "层叠纸雕", "layered paper-cut shadow-box art: the entire scene physically built from 8 to 12 stacked layers of cut colored cardstock inside a deep wooden shadow-box frame, each layer a flat paper silhouette with visible cut edges and paper thickness, soft shadows cast between the layers creating real depth, photographed straight on; no painted details, no gradients, everything is cut paper"),
 (6, "折纸", "origami diorama: everything folded from paper with sharp crease lines, paper texture, minimal clean backdrop"),
 (6, "积木拼搭", "plastic toy brick build: the scene constructed from interlocking toy bricks and minifigure-style characters, glossy plastic, studs visible"),
 (6, "木雕木偶", "carved wooden figures: visible wood grain and chisel marks, painted folk colors, warm handcrafted toy diorama"),
 (6, "低多边形", "low-poly 3D render: faceted geometric polygons, flat shading, soft pastel lighting, minimal"),
 (6, "等距微缩场景", "isometric 3D miniature room diorama: cut-away cube room viewed from 45 degrees, tiny detailed furniture, soft render, floating on a plain background"),
 (6, "移轴微缩摄影", "tilt-shift miniature photography: real scene photographed to look like a tiny model, strong selective blur top and bottom, saturated colors"),
 (6, "盲盒潮玩", "designer vinyl blind-box toy: glossy smooth plastic figures, big head, simplified cute features, product shot on a pastel pedestal"),
 (6, "玻璃透明", "glass sculpture: the whole scene made of transparent colored glass, refractions, caustic light patterns, glossy highlights"),
 (6, "刺绣贴布", "appliqué and embroidery textile art: fabric patches stitched together with visible running stitches and buttons, felt and cotton textures"),
 # 摄影与影视
 (7, "35mm 胶片", "35mm film photograph: Kodak Portra colors, natural grain, soft window light, candid documentary moment"),
 (7, "宝丽来", "Polaroid instant photo: washed-out warm colors, soft focus, light leak, white Polaroid frame border"),
 (7, "黑白纪实", "black-and-white documentary photography: high-contrast silver gelatin print, strong window light, deep grain, humanist street-photography feel"),
 (7, "电影剧照", "cinematic film still: anamorphic widescreen framing, teal and warm orange grading, shallow depth of field, atmospheric light rays"),
 (7, "九十年代港片霓虹", "1990s Hong Kong film cinematography: saturated green and red neon light spilling through the window, step-printed motion blur feel, moody grain"),
 (7, "对称粉彩电影感", "symmetrical pastel cinematography like Wes Anderson: perfectly centered composition, flat frontal view, pastel pink and mint palette, whimsical tidy set"),
 (7, "赛博朋克", "cyberpunk: futuristic city with holographic ads outside the window, magenta and cyan neon glow, rain on glass, high-tech details in the room"),
 (7, "蒸汽波", "vaporwave aesthetic: pink and purple gradient sky, greek statue bust on the sill, retro 90s computer graphics, grid horizon, glitch"),
 (7, "自然纪录片", "nature documentary photography: telephoto shot, natural light, the cat as the wildlife subject in sharp focus, the child softly blurred, National Geographic feel"),
 (7, "产品棚拍", "studio product photography: seamless colored backdrop, softbox lighting, crisp shadows, the scene staged like a premium catalog shot"),
 # 设计与图解
 (8, "瑞士平面", "Swiss International Typographic Style poster: strict grid, Helvetica-like sans-serif headline, flat geometric shapes, red black and white"),
 (8, "包豪斯", "Bauhaus design: primary colors, circles squares and triangles, the scene abstracted into bold geometric forms, modernist typography"),
 (8, "孟菲斯", "Memphis design: playful squiggles, confetti patterns, pastel and bright clashing colors, bold black outlines, 1980s postmodern"),
 (8, "蓝图工程图", "technical blueprint: white line drawing on blueprint blue, measurement annotations, orthographic views of the window seat, grid paper"),
 (8, "博物学插画", "vintage naturalist illustration plate: detailed scientific watercolor of the cat and plant with Latin name labels, numbered specimens, aged paper"),
 (8, "科学解剖图", "educational cutaway diagram: labeled callouts explaining the scene (light, book, plant, cat), clean textbook illustration with leader lines"),
 (8, "信息图", "infographic layout: the scene as a central illustration with icons, short labels, a small chart about reading time, clean modern colors"),
 (8, "手绘地图", "hand-drawn illustrated map of the room: bird's-eye view, cute labeled landmarks (reading nook, cat bed, plant), dotted path, compass rose"),
 (8, "图标集", "icon set: the scene broken into a 3x3 grid of consistent flat line icons (child, book, cat, plant, window, sun, cushion, cup, lamp), same stroke weight"),
]
assert len(STYLES) == 116, len(STYLES)


def prompt(style):
    g, zh, desc = style
    return (f"Style: {desc}.\n\n"
            f"Subject: {SUBJECT_EN}.\n\n"
            f"Render the whole image faithfully in this one style, so the style is instantly recognizable. "
            f"Vertical 3:4 composition. No subtitles, no captions, no watermark, no signature, no logo.\n")
