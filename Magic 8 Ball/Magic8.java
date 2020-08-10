import java.util.Random;
import java.util.*;

public class Magic8 {

    private String[] answers = {"It is certain.", "It is decidedly so.",
      "Without a doubt.", "Yes – definitely.", "You may rely on it.",
      "As I see it, yes.", "Most likely.", "Outlook good.",
      "Yes.", "Signs point to yes.", "Reply hazy, try again.",
      "Ask again later.", "Better not tell you now.", "Cannot predict now.",
      "Concentrate and ask again.", "Don't count on it.", "My reply is no.",
      "My sources say no.", "Outlook not so good.", "Very doubtful."};

    public String getAnswer() {
      int answerInt = new Random().nextInt(20);
      return answers[answerInt];
    }

    public static void main(String[] args) {

      Magic8 magic8Ball = new Magic8();
      Scanner scanner = new Scanner(System.in);

      System.out.println("Java Powered Magic 8 Ball");
      System.out.println("\nAsk a question with a yes or no answer and I predict");
      System.out.print("Enter your question: ");
      String question = scanner.nextLine();

      String answer = magic8Ball.getAnswer();
      System.out.println(answer);

    }

}
