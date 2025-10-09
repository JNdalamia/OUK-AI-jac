with entry {
    num_list=[3, 5, 6, 8, 7, 4];

    num_list[1] = 1;
    print(num_list);

    num_list.append(2);
    print(num_list);

    num_list.insert(4, 0);
    print(num_list);

    num_list.remove(8);
    print(num_list);

    num_list.pop(0);
    print(num_list);

    print(len(num_list));

    more_num = num_list + [3, 5, 8];
    print(more_num);

    repeated = [2] * 6;
    print(repeated);

    if 1 in num_list {
        print("1 is in the list");
    }

    for num in num_list {
        print(num);
    }

    for i = 0 to i < len(num_list) by i -= 1{
        print(f"{i} = {num_list[i]}");
    }