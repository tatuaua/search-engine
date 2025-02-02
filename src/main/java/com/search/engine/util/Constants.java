package com.search.engine.util;

import java.util.Set;

public class Constants {

    public static final String DIRECTORY_PATH = "src/main/resources/input"; // Folder with text files

    public static final Set<String> STOP_WORDS = Set.of(
        "the", "is", "in", "at", "of", "and", "a", "to"
    );
}
