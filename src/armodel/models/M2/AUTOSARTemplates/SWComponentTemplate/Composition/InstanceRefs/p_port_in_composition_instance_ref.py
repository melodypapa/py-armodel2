"""PPortInCompositionInstanceRef AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 951)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_Composition_InstanceRefs.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Composition.InstanceRefs.port_in_composition_type_instance_ref import (
    PortInCompositionTypeInstanceRef,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.abstract_provided_port_prototype import (
    AbstractProvidedPortPrototype,
)


class PPortInCompositionInstanceRef(PortInCompositionTypeInstanceRef):
    """AUTOSAR PPortInCompositionInstanceRef."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    context: Optional[Any]
    target_p_port_prototype: Optional[AbstractProvidedPortPrototype]
    def __init__(self) -> None:
        """Initialize PPortInCompositionInstanceRef."""
        super().__init__()
        self.context: Optional[Any] = None
        self.target_p_port_prototype: Optional[AbstractProvidedPortPrototype] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "PPortInCompositionInstanceRef":
        """Deserialize XML element to PPortInCompositionInstanceRef object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized PPortInCompositionInstanceRef object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse context
        child = ARObject._find_child_element(element, "CONTEXT")
        if child is not None:
            context_value = child.text
            obj.context = context_value

        # Parse target_p_port_prototype
        child = ARObject._find_child_element(element, "TARGET-P-PORT-PROTOTYPE")
        if child is not None:
            target_p_port_prototype_value = ARObject._deserialize_by_tag(child, "AbstractProvidedPortPrototype")
            obj.target_p_port_prototype = target_p_port_prototype_value

        return obj



class PPortInCompositionInstanceRefBuilder:
    """Builder for PPortInCompositionInstanceRef."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: PPortInCompositionInstanceRef = PPortInCompositionInstanceRef()

    def build(self) -> PPortInCompositionInstanceRef:
        """Build and return PPortInCompositionInstanceRef object.

        Returns:
            PPortInCompositionInstanceRef instance
        """
        # TODO: Add validation
        return self._obj
