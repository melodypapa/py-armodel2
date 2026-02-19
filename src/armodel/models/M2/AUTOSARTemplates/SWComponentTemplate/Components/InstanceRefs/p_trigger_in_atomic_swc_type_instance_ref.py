"""PTriggerInAtomicSwcTypeInstanceRef AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 946)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_Components_InstanceRefs.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.InstanceRefs.trigger_in_atomic_swc_instance_ref import (
    TriggerInAtomicSwcInstanceRef,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.abstract_provided_port_prototype import (
    AbstractProvidedPortPrototype,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.TriggerDeclaration.trigger import (
    Trigger,
)


class PTriggerInAtomicSwcTypeInstanceRef(TriggerInAtomicSwcInstanceRef):
    """AUTOSAR PTriggerInAtomicSwcTypeInstanceRef."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    context_p_port_prototype: Optional[AbstractProvidedPortPrototype]
    target_trigger_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize PTriggerInAtomicSwcTypeInstanceRef."""
        super().__init__()
        self.context_p_port_prototype: Optional[AbstractProvidedPortPrototype] = None
        self.target_trigger_ref: Optional[ARRef] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "PTriggerInAtomicSwcTypeInstanceRef":
        """Deserialize XML element to PTriggerInAtomicSwcTypeInstanceRef object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized PTriggerInAtomicSwcTypeInstanceRef object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse context_p_port_prototype
        child = ARObject._find_child_element(element, "CONTEXT-P-PORT-PROTOTYPE")
        if child is not None:
            context_p_port_prototype_value = ARObject._deserialize_by_tag(child, "AbstractProvidedPortPrototype")
            obj.context_p_port_prototype = context_p_port_prototype_value

        # Parse target_trigger_ref
        child = ARObject._find_child_element(element, "TARGET-TRIGGER")
        if child is not None:
            target_trigger_ref_value = ARObject._deserialize_by_tag(child, "Trigger")
            obj.target_trigger_ref = target_trigger_ref_value

        return obj



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
