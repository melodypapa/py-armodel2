"""PModeGroupInAtomicSwcInstanceRef AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 949)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_Components_InstanceRefs.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.InstanceRefs.mode_group_in_atomic_swc_instance_ref import (
    ModeGroupInAtomicSwcInstanceRef,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.abstract_provided_port_prototype import (
    AbstractProvidedPortPrototype,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration.mode_declaration_group import (
    ModeDeclarationGroup,
)


class PModeGroupInAtomicSwcInstanceRef(ModeGroupInAtomicSwcInstanceRef):
    """AUTOSAR PModeGroupInAtomicSwcInstanceRef."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    context_p_port_prototype: Optional[AbstractProvidedPortPrototype]
    target_mode_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize PModeGroupInAtomicSwcInstanceRef."""
        super().__init__()
        self.context_p_port_prototype: Optional[AbstractProvidedPortPrototype] = None
        self.target_mode_ref: Optional[ARRef] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "PModeGroupInAtomicSwcInstanceRef":
        """Deserialize XML element to PModeGroupInAtomicSwcInstanceRef object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized PModeGroupInAtomicSwcInstanceRef object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse context_p_port_prototype
        child = ARObject._find_child_element(element, "CONTEXT-P-PORT-PROTOTYPE")
        if child is not None:
            context_p_port_prototype_value = ARObject._deserialize_by_tag(child, "AbstractProvidedPortPrototype")
            obj.context_p_port_prototype = context_p_port_prototype_value

        # Parse target_mode_ref
        child = ARObject._find_child_element(element, "TARGET-MODE")
        if child is not None:
            target_mode_ref_value = ARObject._deserialize_by_tag(child, "ModeDeclarationGroup")
            obj.target_mode_ref = target_mode_ref_value

        return obj



class PModeGroupInAtomicSwcInstanceRefBuilder:
    """Builder for PModeGroupInAtomicSwcInstanceRef."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: PModeGroupInAtomicSwcInstanceRef = PModeGroupInAtomicSwcInstanceRef()

    def build(self) -> PModeGroupInAtomicSwcInstanceRef:
        """Build and return PModeGroupInAtomicSwcInstanceRef object.

        Returns:
            PModeGroupInAtomicSwcInstanceRef instance
        """
        # TODO: Add validation
        return self._obj
