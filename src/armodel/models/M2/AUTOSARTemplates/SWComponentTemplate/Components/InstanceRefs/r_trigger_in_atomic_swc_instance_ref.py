"""RTriggerInAtomicSwcInstanceRef AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 945)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_Components_InstanceRefs.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.InstanceRefs.trigger_in_atomic_swc_instance_ref import (
    TriggerInAtomicSwcInstanceRef,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.abstract_required_port_prototype import (
    AbstractRequiredPortPrototype,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.TriggerDeclaration.trigger import (
    Trigger,
)


class RTriggerInAtomicSwcInstanceRef(TriggerInAtomicSwcInstanceRef):
    """AUTOSAR RTriggerInAtomicSwcInstanceRef."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    context_r_port_prototype: Optional[AbstractRequiredPortPrototype]
    target_trigger_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize RTriggerInAtomicSwcInstanceRef."""
        super().__init__()
        self.context_r_port_prototype: Optional[AbstractRequiredPortPrototype] = None
        self.target_trigger_ref: Optional[ARRef] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "RTriggerInAtomicSwcInstanceRef":
        """Deserialize XML element to RTriggerInAtomicSwcInstanceRef object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized RTriggerInAtomicSwcInstanceRef object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(RTriggerInAtomicSwcInstanceRef, cls).deserialize(element)

        # Parse context_r_port_prototype
        child = ARObject._find_child_element(element, "CONTEXT-R-PORT-PROTOTYPE")
        if child is not None:
            context_r_port_prototype_value = ARObject._deserialize_by_tag(child, "AbstractRequiredPortPrototype")
            obj.context_r_port_prototype = context_r_port_prototype_value

        # Parse target_trigger_ref
        child = ARObject._find_child_element(element, "TARGET-TRIGGER")
        if child is not None:
            target_trigger_ref_value = ARObject._deserialize_by_tag(child, "Trigger")
            obj.target_trigger_ref = target_trigger_ref_value

        return obj



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
