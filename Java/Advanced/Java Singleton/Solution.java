import java.lang.reflect.*;
import java.util.*;

class Singleton
{
    private static final Singleton instance = new Singleton();
    public String str;

    private Singleton()
    {
    }

    public static Singleton getSingleInstance()
    {
        return instance;
    }
}
