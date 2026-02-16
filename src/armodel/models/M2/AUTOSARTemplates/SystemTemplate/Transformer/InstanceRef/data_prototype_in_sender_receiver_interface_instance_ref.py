"""DataPrototypeInSenderReceiverInterfaceInstanceRef AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Transformer.InstanceRef.data_prototype_in_port_interface_instance_ref import (
    DataPrototypeInPortInterfaceInstanceRef,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.autosar_data_prototype import (
    AutosarDataPrototype,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.data_prototype import (
    DataPrototype,
)


class DataPrototypeInSenderReceiverInterfaceInstanceRef(DataPrototypeInPortInterfaceInstanceRef):
    """AUTOSAR DataPrototypeInSenderReceiverInterfaceInstanceRef."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("base_interface", None, False, False, any (SenderReceiver)),  # baseInterface
        ("context_datas", None, False, True, any (ApplicationComposite)),  # contextDatas
        ("root_data_prototype_in_sr", None, False, False, AutosarDataPrototype),  # rootDataPrototypeInSr
        ("target_data_prototype_in_sr", None, False, False, DataPrototype),  # targetDataPrototypeInSr
    ]

    def __init__(self) -> None:
        """Initialize DataPrototypeInSenderReceiverInterfaceInstanceRef."""
        super().__init__()
        self.base_interface: Optional[Any] = None
        self.context_datas: list[Any] = []
        self.root_data_prototype_in_sr: Optional[AutosarDataPrototype] = None
        self.target_data_prototype_in_sr: Optional[DataPrototype] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert DataPrototypeInSenderReceiverInterfaceInstanceRef to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DataPrototypeInSenderReceiverInterfaceInstanceRef":
        """Create DataPrototypeInSenderReceiverInterfaceInstanceRef from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            DataPrototypeInSenderReceiverInterfaceInstanceRef instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to DataPrototypeInSenderReceiverInterfaceInstanceRef since parent returns ARObject
        return cast("DataPrototypeInSenderReceiverInterfaceInstanceRef", obj)


class DataPrototypeInSenderReceiverInterfaceInstanceRefBuilder:
    """Builder for DataPrototypeInSenderReceiverInterfaceInstanceRef."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DataPrototypeInSenderReceiverInterfaceInstanceRef = DataPrototypeInSenderReceiverInterfaceInstanceRef()

    def build(self) -> DataPrototypeInSenderReceiverInterfaceInstanceRef:
        """Build and return DataPrototypeInSenderReceiverInterfaceInstanceRef object.

        Returns:
            DataPrototypeInSenderReceiverInterfaceInstanceRef instance
        """
        # TODO: Add validation
        return self._obj
