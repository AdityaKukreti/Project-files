
-- drop database bankproject; 
create database bankproject;
use bankproject;








DROP TABLE IF EXISTS `customer`;
CREATE TABLE IF NOT EXISTS `customer` (
  `acno` varchar(16) NOT NULL,
  `name` char(30) DEFAULT NULL,
  `address` varchar(100) DEFAULT NULL,
  `phone` varchar(15) DEFAULT NULL,
  `email` varchar(80) DEFAULT NULL,
  `aadhar_no` varchar(20) DEFAULT NULL,
  `acc_type` varchar(20) DEFAULT NULL,
  `status` char(15),
  `balance` float(15,2) DEFAULT NULL,
  PRIMARY KEY (`acno`)
) ;



INSERT INTO `customer` (`acno`, `name`, `address`, `phone`, `email`, `aadhar_no`, `acc_type`, `status`, `balance`) VALUES
(1543637654352480, 'rakesh kumar', 'cf-4 surya nagar', '987181818', 'support@cbsetoday.com', '123412434545', 'saving', 'active', 12200.00),
(2847583490987650, 'raju vashistha', 'A-75-B Brij vihar', '96734344318', 'raju@cbsetoday.com', '454512434545', 'current', 'active', 10000.00),
(3738495098459769, 'archana', 'cf04 ', '4545456', 'archana@bianrynote.com', '123456564545', 'saving', 'active', 10000.00),
(4847389874839389, 'ashutosh', 'd-100 brij vihar', '1122334455', 'ashu@gmail.com', '112456566576', 'saving', 'close', 56000.00),
(1234567891011128, 'raman singh', 'e-40 radha bihar', '3344556677', 'raman@yahoo.com', '445556564545', 'saving', 'close', 20000.00),
(6748564750987367, 'sam', 'f-12 surya nagar', '1234', 'sam@gmail.com', '123445565656', 'saving', 'active', 22000.00);



DROP TABLE IF EXISTS `transaction`;
CREATE TABLE IF NOT EXISTS `transaction` (
  `tid` int(11) NOT NULL AUTO_INCREMENT,
  `dot` date DEFAULT NULL,
  `amount` int(10) DEFAULT NULL,
  `type` char(20) DEFAULT NULL,
  `acno` varchar(16) DEFAULT NULL,
  PRIMARY KEY (`tid`)
) ;




