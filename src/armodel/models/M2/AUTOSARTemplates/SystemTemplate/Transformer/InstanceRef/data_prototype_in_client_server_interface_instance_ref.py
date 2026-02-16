"""DataPrototypeInClientServerInterfaceInstanceRef AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Transformer.InstanceRef.data_prototype_in_port_interface_instance_ref import (
    DataPrototypeInPortInterfaceInstanceRef,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.autosar_data_prototype import (
    AutosarDataPrototype,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.client_server_interface import (
    ClientServerInterface,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.data_prototype import (
    DataPrototype,
)


class DataPrototypeInClientServerInterfaceInstanceRef(DataPrototypeInPortInterfaceInstanceRef):
    """AUTOSAR DataPrototypeInClientServerInterfaceInstanceRef."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("base", None, False, False, ClientServerInterface),  # base
        ("context_datas", None, False, True, any (ApplicationComposite)),  # contextDatas
        ("root_data_prototype_in_cs", None, False, False, AutosarDataPrototype),  # rootDataPrototypeInCs
        ("target_data_prototype_in_cs", None, False, False, DataPrototype),  # targetDataPrototypeInCs
    ]

    def __init__(self) -> None:
        """Initialize DataPrototypeInClientServerInterfaceInstanceRef."""
        super().__init__()
        self.base: Optional[ClientServerInterface] = None
        self.context_datas: list[Any] = []
        self.root_data_prototype_in_cs: Optional[AutosarDataPrototype] = None
        self.target_data_prototype_in_cs: Optional[DataPrototype] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert DataPrototypeInClientServerInterfaceInstanceRef to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DataPrototypeInClientServerInterfaceInstanceRef":
        """Create DataPrototypeInClientServerInterfaceInstanceRef from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            DataPrototypeInClientServerInterfaceInstanceRef instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to DataPrototypeInClientServerInterfaceInstanceRef since parent returns ARObject
        return cast("DataPrototypeInClientServerInterfaceInstanceRef", obj)


class DataPrototypeInClientServerInterfaceInstanceRefBuilder:
    """Builder for DataPrototypeInClientServerInterfaceInstanceRef."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DataPrototypeInClientServerInterfaceInstanceRef = DataPrototypeInClientServerInterfaceInstanceRef()

    def build(self) -> DataPrototypeInClientServerInterfaceInstanceRef:
        """Build and return DataPrototypeInClientServerInterfaceInstanceRef object.

        Returns:
            DataPrototypeInClientServerInterfaceInstanceRef instance
        """
        # TODO: Add validation
        return self._obj
