# Regolith

Regolith is an Addon Compiler for the Bedrock Edition of Minecraft. 

Much like `bridge v2`, Regolith introduces the concept of a "project folder", where your addons are written, including the RP, the BP, and any models, textures or configuration files. This single-folder-structure is great for version control, and allows you to keep  your "source-of-truth" outside of `com.mojang`.

In the simplest case, Regolith allows you to "compile" (copy) your RP and BP from the project folder, into the com.mojang folder. During the copy, Regolith will run a series of "filters" on the files, allowing you to programmatically transform them as they are copied into `com.mojang`. This allows you to transform your addon non-destructively, and to introduce new syntax into addons.