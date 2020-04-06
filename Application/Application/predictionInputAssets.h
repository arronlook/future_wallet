#ifndef PREDICTIONINPUTASSETS_H
#define PREDICTIONINPUTASSETS_H

#include <QWidget>
class Controller; // Forward declaration to resolve circular dependency
#include "Controller.h"

namespace Ui {
class predictionInputAssets;
}

class predictionInputAssets : public QWidget
{
    Q_OBJECT

public:
    explicit predictionInputAssets(QWidget *parent = nullptr, Controller * controller = nullptr);
    ~predictionInputAssets();

private:
    Ui::predictionInputAssets *ui;
    Controller * controller;

private slots:
    void submitInputs();
    void getWagesView();
    void Exit();
};

#endif // PREDICTIONINPUTASSETS_H
