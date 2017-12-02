package org.imlv_prabhat_satyendra.studentprosearch;

/**
 * Wrapper class for the message produced by the bot.
 */
public class BotChatMessage extends ChatMessage {

    private boolean typing;

    public BotChatMessage(String message) {
        super(message, false);
        typing = true;
    }

    public boolean isTyping() {
        return typing;
    }

    public BotChatMessage setTyping(boolean typing) {
        this.typing = typing;
        return this;
    }
}
