-- =========================
-- COLLECTIONS
-- =========================
delete from store_collection;
insert into store_collection (id, title, featured_product_id)
values
(1, 'Grocery', null),
(2, 'Beauty', null),
(3, 'Cleaning', null),
(4, 'Spices', null),
(5, 'Toys', null),
(6, 'Electronics', null),
(7, 'Books', null),
(8, 'Pet Supplies', null),
(9, 'Office', null),
(10, 'Fitness', null);


-- =========================
-- PRODUCTS
-- =========================
insert into store_product
(id, title, slug, description, unit_price, inventory, last_updated, collection_id)
values

-- Grocery
(1, 'Organic Milk', 'organic-milk', 'Fresh organic whole milk', 4.99, 120, now(), 1),
(2, 'Brown Bread', 'brown-bread', 'Healthy whole grain bread', 2.99, 85, now(), 1),
(3, 'Eggs Pack', 'eggs-pack', '12 farm fresh eggs', 3.49, 200, now(), 1),
(4, 'Rice 5kg', 'rice-5kg', 'Premium jasmine rice', 11.99, 60, now(), 1),
(5, 'Pasta', 'pasta', 'Italian durum wheat pasta', 2.49, 140, now(), 1),
(6, 'Olive Oil', 'olive-oil', 'Extra virgin olive oil', 8.99, 75, now(), 1),
(7, 'Orange Juice', 'orange-juice', 'Freshly squeezed juice', 5.49, 50, now(), 1),
(8, 'Peanut Butter', 'peanut-butter', 'Creamy peanut spread', 4.79, 90, now(), 1),
(9, 'Corn Flakes', 'corn-flakes', 'Breakfast cereal', 3.99, 70, now(), 1),
(10, 'Cheese Slices', 'cheese-slices', 'Cheddar slices', 4.29, 95, now(), 1),
(11, 'Yogurt', 'yogurt', 'Greek yogurt', 1.99, 110, now(), 1),
(12, 'Bananas', 'bananas', 'Fresh bananas', 1.49, 180, now(), 1),

-- Beauty
(13, 'Face Wash', 'face-wash', 'Gentle skin cleanser', 6.99, 100, now(), 2),
(14, 'Shampoo', 'shampoo', 'Herbal anti-dandruff shampoo', 7.49, 90, now(), 2),
(15, 'Conditioner', 'conditioner', 'Smooth hair conditioner', 7.99, 88, now(), 2),
(16, 'Lip Balm', 'lip-balm', 'Moisturizing lip care', 2.99, 130, now(), 2),
(17, 'Body Lotion', 'body-lotion', 'Hydrating lotion', 5.99, 75, now(), 2),
(18, 'Perfume', 'perfume', 'Long lasting fragrance', 19.99, 40, now(), 2),
(19, 'Sunscreen', 'sunscreen', 'SPF 50 protection', 9.99, 60, now(), 2),
(20, 'Hair Oil', 'hair-oil', 'Natural coconut oil', 4.99, 100, now(), 2),
(21, 'Soap Bar', 'soap-bar', 'Lavender soap', 1.99, 160, now(), 2),
(22, 'Face Cream', 'face-cream', 'Night repair cream', 11.99, 55, now(), 2),
(23, 'Nail Polish', 'nail-polish', 'Glossy red polish', 3.49, 70, now(), 2),
(24, 'Makeup Kit', 'makeup-kit', 'Beginner beauty kit', 24.99, 25, now(), 2),

-- Cleaning
(25, 'Dish Soap', 'dish-soap', 'Lemon dishwashing liquid', 3.99, 90, now(), 3),
(26, 'Floor Cleaner', 'floor-cleaner', 'Pine floor cleaner', 6.49, 70, now(), 3),
(27, 'Glass Spray', 'glass-spray', 'Streak-free cleaner', 4.99, 60, now(), 3),
(28, 'Laundry Detergent', 'laundry-detergent', 'Liquid detergent', 12.99, 50, now(), 3),
(29, 'Bleach', 'bleach', 'Strong disinfectant bleach', 5.99, 45, now(), 3),
(30, 'Sponges', 'sponges', 'Pack of 6 sponges', 2.49, 100, now(), 3),
(31, 'Trash Bags', 'trash-bags', '30 gallon trash bags', 7.99, 65, now(), 3),
(32, 'Toilet Cleaner', 'toilet-cleaner', 'Deep clean gel', 4.49, 55, now(), 3),
(33, 'Air Freshener', 'air-freshener', 'Ocean breeze scent', 3.99, 80, now(), 3),
(34, 'Disinfectant Wipes', 'disinfectant-wipes', 'Pack of 80 wipes', 5.49, 85, now(), 3),
(35, 'Mop Refill', 'mop-refill', 'Microfiber refill', 6.99, 40, now(), 3),
(36, 'Rubber Gloves', 'rubber-gloves', 'Cleaning gloves pair', 2.99, 120, now(), 3),

-- Spices
(37, 'Turmeric', 'turmeric', 'Ground turmeric powder', 2.99, 100, now(), 4),
(38, 'Black Pepper', 'black-pepper', 'Fine black pepper', 3.49, 95, now(), 4),
(39, 'Cumin', 'cumin', 'Whole cumin seeds', 2.79, 90, now(), 4),
(40, 'Paprika', 'paprika', 'Smoked paprika', 3.99, 80, now(), 4),
(41, 'Cinnamon', 'cinnamon', 'Ground cinnamon', 4.29, 75, now(), 4),
(42, 'Cloves', 'cloves', 'Whole cloves', 3.99, 60, now(), 4),
(43, 'Nutmeg', 'nutmeg', 'Aromatic nutmeg', 4.49, 55, now(), 4),
(44, 'Cardamom', 'cardamom', 'Green cardamom pods', 5.99, 45, now(), 4),
(45, 'Chili Flakes', 'chili-flakes', 'Hot red flakes', 2.49, 110, now(), 4),
(46, 'Oregano', 'oregano', 'Dried oregano', 2.99, 85, now(), 4),
(47, 'Bay Leaves', 'bay-leaves', 'Dried bay leaves', 2.29, 70, now(), 4),
(48, 'Garlic Powder', 'garlic-powder', 'Fine garlic powder', 2.89, 100, now(), 4),

-- Toys
(49, 'Toy Car', 'toy-car', 'Mini racing car', 6.99, 100, now(), 5),
(50, 'Doll House', 'doll-house', 'Wooden doll house', 29.99, 20, now(), 5),
(51, 'Puzzle Set', 'puzzle-set', '500 piece puzzle', 9.99, 60, now(), 5),
(52, 'Building Blocks', 'building-blocks', 'Creative blocks set', 19.99, 40, now(), 5),
(53, 'Action Figure', 'action-figure', 'Hero action figure', 14.99, 35, now(), 5),
(54, 'Board Game', 'board-game', 'Family board game', 24.99, 30, now(), 5),
(55, 'Water Gun', 'water-gun', 'Summer water toy', 7.99, 75, now(), 5),
(56, 'Stuffed Bear', 'stuffed-bear', 'Soft teddy bear', 12.99, 45, now(), 5),
(57, 'Yo-Yo', 'yo-yo', 'Classic yo-yo toy', 3.49, 90, now(), 5),
(58, 'Remote Drone', 'remote-drone', 'Mini drone', 49.99, 15, now(), 5),
(59, 'Toy Train', 'toy-train', 'Electric train toy', 34.99, 18, now(), 5),
(60, 'Coloring Kit', 'coloring-kit', 'Kids art set', 8.99, 55, now(), 5),

-- Electronics
(61, 'USB Cable', 'usb-cable', 'Fast charging cable', 5.99, 120, now(), 6),
(62, 'Wireless Mouse', 'wireless-mouse', 'Ergonomic mouse', 14.99, 70, now(), 6),
(63, 'Keyboard', 'keyboard', 'Mechanical keyboard', 39.99, 40, now(), 6),
(64, 'Phone Charger', 'phone-charger', '20W wall charger', 12.99, 80, now(), 6),
(65, 'Bluetooth Speaker', 'bluetooth-speaker', 'Portable speaker', 29.99, 35, now(), 6),
(66, 'Power Bank', 'power-bank', '10000mAh battery pack', 24.99, 50, now(), 6),
(67, 'Webcam', 'webcam', 'HD webcam', 34.99, 25, now(), 6),
(68, 'Headphones', 'headphones', 'Noise cancelling', 59.99, 20, now(), 6),
(69, 'Smart Watch', 'smart-watch', 'Fitness smartwatch', 89.99, 18, now(), 6),
(70, 'LED Lamp', 'led-lamp', 'Desk LED lamp', 22.99, 45, now(), 6),
(71, 'Monitor Stand', 'monitor-stand', 'Adjustable stand', 27.99, 30, now(), 6),
(72, 'SSD 1TB', 'ssd-1tb', 'Solid state drive', 99.99, 22, now(), 6),

-- Books
(73, 'Python Basics', 'python-basics', 'Programming guide', 19.99, 50, now(), 7),
(74, 'SQL Mastery', 'sql-mastery', 'Advanced SQL book', 24.99, 40, now(), 7),
(75, 'Django in Action', 'django-in-action', 'Web dev with Django', 29.99, 35, now(), 7),
(76, 'Clean Code', 'clean-code', 'Software craftsmanship', 31.99, 25, now(), 7),
(77, 'Data Structures', 'data-structures', 'CS fundamentals', 27.99, 30, now(), 7),
(78, 'Machine Learning', 'machine-learning', 'ML concepts', 34.99, 20, now(), 7),
(79, 'Algorithms', 'algorithms', 'Problem solving', 28.99, 22, now(), 7),
(80, 'Design Patterns', 'design-patterns', 'Reusable OOP patterns', 26.99, 18, now(), 7),
(81, 'System Design', 'system-design', 'Scalable systems', 32.99, 20, now(), 7),
(82, 'Docker Guide', 'docker-guide', 'Containers and deployment', 21.99, 28, now(), 7),
(83, 'Kubernetes Intro', 'kubernetes-intro', 'Orchestration basics', 23.99, 26, now(), 7),
(84, 'REST APIs', 'rest-apis', 'API development guide', 18.99, 33, now(), 7),

-- Pet Supplies
(85, 'Dog Food', 'dog-food', 'Premium dog food', 18.99, 60, now(), 8),
(86, 'Cat Food', 'cat-food', 'Salmon cat food', 16.99, 55, now(), 8),
(87, 'Pet Shampoo', 'pet-shampoo', 'Gentle pet wash', 7.99, 40, now(), 8),
(88, 'Leash', 'leash', 'Durable dog leash', 9.99, 70, now(), 8),
(89, 'Pet Bed', 'pet-bed', 'Soft sleeping bed', 24.99, 25, now(), 8),
(90, 'Bird Seeds', 'bird-seeds', 'Mixed bird seeds', 6.99, 50, now(), 8),
(91, 'Fish Flakes', 'fish-flakes', 'Aquarium fish food', 4.99, 65, now(), 8),
(92, 'Cat Toy', 'cat-toy', 'Feather teaser', 3.99, 90, now(), 8),
(93, 'Dog Bowl', 'dog-bowl', 'Steel bowl', 8.49, 45, now(), 8),
(94, 'Pet Brush', 'pet-brush', 'De-shedding brush', 10.99, 35, now(), 8),
(95, 'Aquarium Filter', 'aquarium-filter', 'Water filter', 29.99, 15, now(), 8),
(96, 'Hamster Wheel', 'hamster-wheel', 'Silent wheel', 11.99, 20, now(), 8),

-- Office
(97, 'Notebook', 'notebook', '200 page notebook', 3.49, 150, now(), 9),
(98, 'Pen Set', 'pen-set', 'Pack of 10 pens', 4.99, 140, now(), 9),
(99, 'Stapler', 'stapler', 'Heavy duty stapler', 8.99, 50, now(), 9),
(100, 'Printer Paper', 'printer-paper', '500 sheet ream', 6.99, 90, now(), 9),
(101, 'Desk Organizer', 'desk-organizer', 'Wood organizer', 14.99, 30, now(), 9),
(102, 'Whiteboard', 'whiteboard', 'Magnetic whiteboard', 39.99, 12, now(), 9),
(103, 'Markers', 'markers', 'Pack of 8 markers', 5.99, 80, now(), 9),
(104, 'Sticky Notes', 'sticky-notes', 'Color sticky notes', 2.99, 100, now(), 9),
(105, 'Paper Clips', 'paper-clips', '100 clips box', 1.99, 120, now(), 9),
(106, 'File Folder', 'file-folder', 'Document folder', 3.99, 95, now(), 9),
(107, 'Calculator', 'calculator', 'Office calculator', 12.99, 35, now(), 9),
(108, 'Desk Chair', 'desk-chair', 'Ergonomic chair', 129.99, 10, now(), 9),

-- Fitness
(109, 'Yoga Mat', 'yoga-mat', 'Non-slip yoga mat', 19.99, 50, now(), 10),
(110, 'Dumbbells', 'dumbbells', '10kg pair', 34.99, 25, now(), 10),
(111, 'Resistance Bands', 'resistance-bands', 'Set of 5 bands', 14.99, 60, now(), 10),
(112, 'Protein Shaker', 'protein-shaker', 'Leakproof bottle', 8.99, 80, now(), 10),
(113, 'Skipping Rope', 'skipping-rope', 'Adjustable rope', 6.99, 75, now(), 10),
(114, 'Pull Up Bar', 'pull-up-bar', 'Door frame bar', 29.99, 20, now(), 10),
(115, 'Foam Roller', 'foam-roller', 'Muscle recovery roller', 16.99, 35, now(), 10),
(116, 'Kettlebell', 'kettlebell', '12kg kettlebell', 27.99, 18, now(), 10),
(117, 'Gym Gloves', 'gym-gloves', 'Weight lifting gloves', 9.99, 55, now(), 10),
(118, 'Treadmill', 'treadmill', 'Home treadmill', 499.99, 5, now(), 10),
(119, 'Exercise Ball', 'exercise-ball', '65cm ball', 18.99, 28, now(), 10),
(120, 'Fitness Tracker', 'fitness-tracker', 'Step and heart rate monitor', 59.99, 22, now(), 10);