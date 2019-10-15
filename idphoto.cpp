#include "idphoto.h"
#include "ui_idphoto.h"

IDPhoto::IDPhoto(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::IDPhoto)
{
    ui->setupUi(this);
}

IDPhoto::~IDPhoto()
{
    delete ui;
}
