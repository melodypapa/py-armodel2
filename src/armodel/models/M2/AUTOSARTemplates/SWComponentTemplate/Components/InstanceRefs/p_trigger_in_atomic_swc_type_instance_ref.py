"""PTriggerInAtomicSwcTypeInstanceRef AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.InstanceRefs.trigger_in_atomic_swc_instance_ref import (
    TriggerInAtomicSwcInstanceRef,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.abstract_provided_port_prototype import (
    AbstractProvidedPortPrototype,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.TriggerDeclaration.trigger import (
    Trigger,
)


class PTriggerInAtomicSwcTypeInstanceRef(TriggerInAtomicSwcInstanceRef):
    """AUTOSAR PTriggerInAtomicSwcTypeInstanceRef."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("context_p_port_prototype", None, False, False, AbstractProvidedPortPrototype),  # contextPPortPrototype
        ("target_trigger", None, False, False, Trigger),  # targetTrigger
    ]

    def __init__(self) -> None:
        """Initialize PTriggerInAtomicSwcTypeInstanceRef."""
        super().__init__()
        self.context_p_port_prototype: Optional[AbstractProvidedPortPrototype] = None
        self.target_trigger: Optional[Trigger] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert PTriggerInAtomicSwcTypeInstanceRef to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "PTriggerInAtomicSwcTypeInstanceRef":
        """Create PTriggerInAtomicSwcTypeInstanceRef from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            PTriggerInAtomicSwcTypeInstanceRef instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to PTriggerInAtomicSwcTypeInstanceRef since parent returns ARObject
        return cast("PTriggerInAtomicSwcTypeInstanceRef", obj)


class PTriggerInAtomicSwcTypeInstanceRefBuilder:
    """Builder for PTriggerInAtomicSwcTypeInstanceRef."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: PTriggerInAtomicSwcTypeInstanceRef = PTriggerInAtomicSwcTypeInstanceRef()

    def build(self) -> PTriggerInAtomicSwcTypeInstanceRef:
        """Build and return PTriggerInAtomicSwcTypeInstanceRef object.

        Returns:
            PTriggerInAtomicSwcTypeInstanceRef instance
        """
        # TODO: Add validation
        return self._obj
