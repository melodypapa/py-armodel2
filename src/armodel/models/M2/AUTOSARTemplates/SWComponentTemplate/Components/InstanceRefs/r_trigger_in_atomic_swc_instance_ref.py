"""RTriggerInAtomicSwcInstanceRef AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.InstanceRefs.trigger_in_atomic_swc_instance_ref import (
    TriggerInAtomicSwcInstanceRef,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.abstract_required_port_prototype import (
    AbstractRequiredPortPrototype,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.TriggerDeclaration.trigger import (
    Trigger,
)


class RTriggerInAtomicSwcInstanceRef(TriggerInAtomicSwcInstanceRef):
    """AUTOSAR RTriggerInAtomicSwcInstanceRef."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("context_r_port_prototype", None, False, False, AbstractRequiredPortPrototype),  # contextRPortPrototype
        ("target_trigger", None, False, False, Trigger),  # targetTrigger
    ]

    def __init__(self) -> None:
        """Initialize RTriggerInAtomicSwcInstanceRef."""
        super().__init__()
        self.context_r_port_prototype: Optional[AbstractRequiredPortPrototype] = None
        self.target_trigger: Optional[Trigger] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert RTriggerInAtomicSwcInstanceRef to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "RTriggerInAtomicSwcInstanceRef":
        """Create RTriggerInAtomicSwcInstanceRef from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            RTriggerInAtomicSwcInstanceRef instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to RTriggerInAtomicSwcInstanceRef since parent returns ARObject
        return cast("RTriggerInAtomicSwcInstanceRef", obj)


class RTriggerInAtomicSwcInstanceRefBuilder:
    """Builder for RTriggerInAtomicSwcInstanceRef."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: RTriggerInAtomicSwcInstanceRef = RTriggerInAtomicSwcInstanceRef()

    def build(self) -> RTriggerInAtomicSwcInstanceRef:
        """Build and return RTriggerInAtomicSwcInstanceRef object.

        Returns:
            RTriggerInAtomicSwcInstanceRef instance
        """
        # TODO: Add validation
        return self._obj
