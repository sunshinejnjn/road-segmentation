class Config():
    num_epochs = 50
    validation_summary_frequency = 1000
    checkpoint_frequency = 1000
    batch_size = 32
    log_directory = 'logs/'
    examples_to_show = 5
    image_size = 400
    post_process_patch_size = 8
    train_image_size = image_size // post_process_patch_size
    train_size = 100
    dropout_train = 0.5