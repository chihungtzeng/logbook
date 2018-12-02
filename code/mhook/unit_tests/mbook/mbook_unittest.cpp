#include <mbook.h>
#include <iostream>
#include <gtest/gtest.h>

TEST(MbookTest, M_INIT_PEAK){
    MBook mbook;
    ASSERT_EQ(0, mbook.get_peak());
    ASSERT_EQ(0, mbook.get_current_usage());
}

TEST(MbookTest, M_ADD_RECORD_NO_CONFLICT){
    MBook mbook;
    mbook.add_record(0x1234, 10);
    mbook.add_record(0x1235, 20);
    ASSERT_EQ(10 + 20, mbook.get_peak());
    ASSERT_EQ(10 + 20, mbook.get_current_usage());
}

TEST(MbookTest, M_ADD_RECORD_CONFLICT){
    MBook mbook;
    mbook.add_record(0x1234, 10);
    mbook.add_record(0x1234, 30);
    ASSERT_EQ(30, mbook.get_peak());
    ASSERT_EQ(30, mbook.get_current_usage());

    mbook.add_record(0x1234, 20);
    ASSERT_EQ(30, mbook.get_peak());
    ASSERT_EQ(20, mbook.get_current_usage());

    mbook.add_record(0x1234, 10);
    mbook.add_record(0x1235, 5);
    ASSERT_EQ(30, mbook.get_peak());
    ASSERT_EQ(10 + 5, mbook.get_current_usage());
}




