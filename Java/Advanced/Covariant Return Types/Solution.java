class Flower
{
    public String whatsYourName()
    {
        return "I have many names and types.";
    }
}

class Jasmine extends Flower
{
    @Override
    public String whatsYourName()
    {
        return this.getClass().getName();
    }
}

class Lily extends Flower
{
    @Override
    public String whatsYourName()
    {
        return this.getClass().getName();
    }
}

class Lotus extends Flower
{
    @Override
    public String whatsYourName()
    {
        return this.getClass().getName();
    }
}

class State
{
    Flower yourNationalFlower()
    {
        return new Flower();
    }
}

class WestBengal extends State
{
    @Override
    Flower yourNationalFlower()
    {
        return new Jasmine();
    }
}

class Karnataka extends State
{
    @Override
    Flower yourNationalFlower()
    {
        return new Lotus();
    }
}

class AndhraPradesh extends State
{
    @Override
    Flower yourNationalFlower()
    {
        return new Lily();
    }
}
