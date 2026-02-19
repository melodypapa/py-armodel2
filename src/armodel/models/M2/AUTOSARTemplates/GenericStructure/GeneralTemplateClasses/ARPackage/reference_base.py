"""ReferenceBase AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 72)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_GenericStructure_GeneralTemplateClasses_ARPackage.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    Identifier,
    ReferrableSubtypesEnum,
)

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_package import (
        ARPackage,
    )



class ReferenceBase(ARObject):
    """AUTOSAR ReferenceBase."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    global_element_refs: list[ARRef]
    global_ins: list[ARPackage]
    is_default: Boolean
    package: Optional[ARPackage]
    short_label: Identifier
    def __init__(self) -> None:
        """Initialize ReferenceBase."""
        super().__init__()
        self.global_element_refs: list[ARRef] = []
        self.global_ins: list[ARPackage] = []
        self.is_default: Boolean = None
        self.package: Optional[ARPackage] = None
        self.short_label: Identifier = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "ReferenceBase":
        """Deserialize XML element to ReferenceBase object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ReferenceBase object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse global_element_refs (list)
        obj.global_element_refs = []
        for child in ARObject._find_all_child_elements(element, "GLOBAL-ELEMENTS"):
            global_element_refs_value = child.text
            obj.global_element_refs.append(global_element_refs_value)

        # Parse global_ins (list)
        obj.global_ins = []
        for child in ARObject._find_all_child_elements(element, "GLOBAL-INS"):
            global_ins_value = ARObject._deserialize_by_tag(child, "ARPackage")
            obj.global_ins.append(global_ins_value)

        # Parse is_default
        child = ARObject._find_child_element(element, "IS-DEFAULT")
        if child is not None:
            is_default_value = child.text
            obj.is_default = is_default_value

        # Parse package
        child = ARObject._find_child_element(element, "PACKAGE")
        if child is not None:
            package_value = ARObject._deserialize_by_tag(child, "ARPackage")
            obj.package = package_value

        # Parse short_label
        child = ARObject._find_child_element(element, "SHORT-LABEL")
        if child is not None:
            short_label_value = child.text
            obj.short_label = short_label_value

        return obj



class ReferenceBaseBuilder:
    """Builder for ReferenceBase."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ReferenceBase = ReferenceBase()

    def build(self) -> ReferenceBase:
        """Build and return ReferenceBase object.

        Returns:
            ReferenceBase instance
        """
        # TODO: Add validation
        return self._obj
