"""EngineeringObject AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 132)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 160)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_GenericStructure_GeneralTemplateClasses_EngineeringObject.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    NameToken,
    RevisionLabelString,
)
from abc import ABC, abstractmethod


class EngineeringObject(ARObject, ABC):
    """AUTOSAR EngineeringObject."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    category: NameToken
    domain: Optional[NameToken]
    revision_label_strings: list[RevisionLabelString]
    short_label: NameToken
    def __init__(self) -> None:
        """Initialize EngineeringObject."""
        super().__init__()
        self.category: NameToken = None
        self.domain: Optional[NameToken] = None
        self.revision_label_strings: list[RevisionLabelString] = []
        self.short_label: NameToken = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "EngineeringObject":
        """Deserialize XML element to EngineeringObject object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized EngineeringObject object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse category
        child = ARObject._find_child_element(element, "CATEGORY")
        if child is not None:
            category_value = child.text
            obj.category = category_value

        # Parse domain
        child = ARObject._find_child_element(element, "DOMAIN")
        if child is not None:
            domain_value = child.text
            obj.domain = domain_value

        # Parse revision_label_strings (list)
        obj.revision_label_strings = []
        for child in ARObject._find_all_child_elements(element, "REVISION-LABEL-STRINGS"):
            revision_label_strings_value = child.text
            obj.revision_label_strings.append(revision_label_strings_value)

        # Parse short_label
        child = ARObject._find_child_element(element, "SHORT-LABEL")
        if child is not None:
            short_label_value = child.text
            obj.short_label = short_label_value

        return obj



class EngineeringObjectBuilder:
    """Builder for EngineeringObject."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: EngineeringObject = EngineeringObject()

    def build(self) -> EngineeringObject:
        """Build and return EngineeringObject object.

        Returns:
            EngineeringObject instance
        """
        # TODO: Add validation
        return self._obj
