#ifndef IDPHOTO_H
#define IDPHOTO_H

#include <QMainWindow>

namespace Ui {
class IDPhoto;
}

class IDPhoto : public QMainWindow
{
    Q_OBJECT

public:
    explicit IDPhoto(QWidget *parent = nullptr);
    ~IDPhoto();

private:
    Ui::IDPhoto *ui;
};

#endif // IDPHOTO_H
