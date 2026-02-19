"""SwcServiceDependencyInSystemInstanceRef AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 369)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_InstanceRefs.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.root_sw_composition_prototype import (
    RootSwCompositionPrototype,
)


class SwcServiceDependencyInSystemInstanceRef(ARObject):
    """AUTOSAR SwcServiceDependencyInSystemInstanceRef."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    context_root_sw: Optional[RootSwCompositionPrototype]
    context_sw_prototypes: list[Any]
    target_swc: Optional[Any]
    def __init__(self) -> None:
        """Initialize SwcServiceDependencyInSystemInstanceRef."""
        super().__init__()
        self.context_root_sw: Optional[RootSwCompositionPrototype] = None
        self.context_sw_prototypes: list[Any] = []
        self.target_swc: Optional[Any] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "SwcServiceDependencyInSystemInstanceRef":
        """Deserialize XML element to SwcServiceDependencyInSystemInstanceRef object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SwcServiceDependencyInSystemInstanceRef object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse context_root_sw
        child = ARObject._find_child_element(element, "CONTEXT-ROOT-SW")
        if child is not None:
            context_root_sw_value = ARObject._deserialize_by_tag(child, "RootSwCompositionPrototype")
            obj.context_root_sw = context_root_sw_value

        # Parse context_sw_prototypes (list)
        obj.context_sw_prototypes = []
        for child in ARObject._find_all_child_elements(element, "CONTEXT-SW-PROTOTYPES"):
            context_sw_prototypes_value = child.text
            obj.context_sw_prototypes.append(context_sw_prototypes_value)

        # Parse target_swc
        child = ARObject._find_child_element(element, "TARGET-SWC")
        if child is not None:
            target_swc_value = child.text
            obj.target_swc = target_swc_value

        return obj



class SwcServiceDependencyInSystemInstanceRefBuilder:
    """Builder for SwcServiceDependencyInSystemInstanceRef."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SwcServiceDependencyInSystemInstanceRef = SwcServiceDependencyInSystemInstanceRef()

    def build(self) -> SwcServiceDependencyInSystemInstanceRef:
        """Build and return SwcServiceDependencyInSystemInstanceRef object.

        Returns:
            SwcServiceDependencyInSystemInstanceRef instance
        """
        # TODO: Add validation
        return self._obj
