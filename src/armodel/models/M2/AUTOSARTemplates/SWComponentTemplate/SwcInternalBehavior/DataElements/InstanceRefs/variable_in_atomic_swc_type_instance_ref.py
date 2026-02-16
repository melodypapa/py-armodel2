"""VariableInAtomicSWCTypeInstanceRef AUTOSAR element."""

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
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.variable_data_prototype import (
    VariableDataPrototype,
)


class VariableInAtomicSWCTypeInstanceRef(ARObject):
    """AUTOSAR VariableInAtomicSWCTypeInstanceRef."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("base", None, False, False, AtomicSwComponentType),  # base
        ("context_datas", None, False, True, any (ApplicationComposite)),  # contextDatas
        ("port_prototype", None, False, False, PortPrototype),  # portPrototype
        ("root_variable_data_prototype", None, False, False, VariableDataPrototype),  # rootVariableDataPrototype
        ("target_data", None, False, False, DataPrototype),  # targetData
    ]

    def __init__(self) -> None:
        """Initialize VariableInAtomicSWCTypeInstanceRef."""
        super().__init__()
        self.base: Optional[AtomicSwComponentType] = None
        self.context_datas: list[Any] = []
        self.port_prototype: Optional[PortPrototype] = None
        self.root_variable_data_prototype: Optional[VariableDataPrototype] = None
        self.target_data: Optional[DataPrototype] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert VariableInAtomicSWCTypeInstanceRef to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "VariableInAtomicSWCTypeInstanceRef":
        """Create VariableInAtomicSWCTypeInstanceRef from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            VariableInAtomicSWCTypeInstanceRef instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to VariableInAtomicSWCTypeInstanceRef since parent returns ARObject
        return cast("VariableInAtomicSWCTypeInstanceRef", obj)


class VariableInAtomicSWCTypeInstanceRefBuilder:
    """Builder for VariableInAtomicSWCTypeInstanceRef."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: VariableInAtomicSWCTypeInstanceRef = VariableInAtomicSWCTypeInstanceRef()

    def build(self) -> VariableInAtomicSWCTypeInstanceRef:
        """Build and return VariableInAtomicSWCTypeInstanceRef object.

        Returns:
            VariableInAtomicSWCTypeInstanceRef instance
        """
        # TODO: Add validation
        return self._obj
