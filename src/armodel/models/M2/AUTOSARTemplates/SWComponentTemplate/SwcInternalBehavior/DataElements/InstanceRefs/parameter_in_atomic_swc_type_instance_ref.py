"""ParameterInAtomicSWCTypeInstanceRef AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.atomic_sw_component_type import (
    AtomicSwComponentType,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.data_prototype import (
    DataPrototype,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.port_prototype import (
    PortPrototype,
)


class ParameterInAtomicSWCTypeInstanceRef(ARObject):
    """AUTOSAR ParameterInAtomicSWCTypeInstanceRef."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("base", None, False, False, AtomicSwComponentType),  # base
        ("context_datas", None, False, True, any (ApplicationComposite)),  # contextDatas
        ("port_prototype", None, False, False, PortPrototype),  # portPrototype
        ("root_parameter", None, False, False, DataPrototype),  # rootParameter
        ("target_data", None, False, False, DataPrototype),  # targetData
    ]

    def __init__(self) -> None:
        """Initialize ParameterInAtomicSWCTypeInstanceRef."""
        super().__init__()
        self.base: Optional[AtomicSwComponentType] = None
        self.context_datas: list[Any] = []
        self.port_prototype: Optional[PortPrototype] = None
        self.root_parameter: Optional[DataPrototype] = None
        self.target_data: Optional[DataPrototype] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert ParameterInAtomicSWCTypeInstanceRef to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ParameterInAtomicSWCTypeInstanceRef":
        """Create ParameterInAtomicSWCTypeInstanceRef from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            ParameterInAtomicSWCTypeInstanceRef instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to ParameterInAtomicSWCTypeInstanceRef since parent returns ARObject
        return cast("ParameterInAtomicSWCTypeInstanceRef", obj)


class ParameterInAtomicSWCTypeInstanceRefBuilder:
    """Builder for ParameterInAtomicSWCTypeInstanceRef."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ParameterInAtomicSWCTypeInstanceRef = ParameterInAtomicSWCTypeInstanceRef()

    def build(self) -> ParameterInAtomicSWCTypeInstanceRef:
        """Build and return ParameterInAtomicSWCTypeInstanceRef object.

        Returns:
            ParameterInAtomicSWCTypeInstanceRef instance
        """
        # TODO: Add validation
        return self._obj
