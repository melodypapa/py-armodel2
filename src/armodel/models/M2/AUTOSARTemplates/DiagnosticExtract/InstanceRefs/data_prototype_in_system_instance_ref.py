"""DataPrototypeInSystemInstanceRef AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.autosar_data_prototype import (
    AutosarDataPrototype,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.data_prototype import (
    DataPrototype,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.port_prototype import (
    PortPrototype,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.root_sw_composition_prototype import (
    RootSwCompositionPrototype,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.system import (
    System,
)


class DataPrototypeInSystemInstanceRef(ARObject):
    """AUTOSAR DataPrototypeInSystemInstanceRef."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("base", None, False, False, System),  # base
        ("contexts", None, False, True, any (SwComponent)),  # contexts
        ("context_datas", None, False, True, any (ApplicationComposite)),  # contextDatas
        ("context_port", None, False, False, PortPrototype),  # contextPort
        ("context_root", None, False, False, RootSwCompositionPrototype),  # contextRoot
        ("root_data_prototype", None, False, False, AutosarDataPrototype),  # rootDataPrototype
        ("target_data", None, False, False, DataPrototype),  # targetData
    ]

    def __init__(self) -> None:
        """Initialize DataPrototypeInSystemInstanceRef."""
        super().__init__()
        self.base: Optional[System] = None
        self.contexts: list[Any] = []
        self.context_datas: list[Any] = []
        self.context_port: Optional[PortPrototype] = None
        self.context_root: Optional[RootSwCompositionPrototype] = None
        self.root_data_prototype: Optional[AutosarDataPrototype] = None
        self.target_data: Optional[DataPrototype] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert DataPrototypeInSystemInstanceRef to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DataPrototypeInSystemInstanceRef":
        """Create DataPrototypeInSystemInstanceRef from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            DataPrototypeInSystemInstanceRef instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to DataPrototypeInSystemInstanceRef since parent returns ARObject
        return cast("DataPrototypeInSystemInstanceRef", obj)


class DataPrototypeInSystemInstanceRefBuilder:
    """Builder for DataPrototypeInSystemInstanceRef."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DataPrototypeInSystemInstanceRef = DataPrototypeInSystemInstanceRef()

    def build(self) -> DataPrototypeInSystemInstanceRef:
        """Build and return DataPrototypeInSystemInstanceRef object.

        Returns:
            DataPrototypeInSystemInstanceRef instance
        """
        # TODO: Add validation
        return self._obj
