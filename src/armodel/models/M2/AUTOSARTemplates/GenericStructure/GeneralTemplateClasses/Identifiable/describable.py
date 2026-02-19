"""Describable AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 312)
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 293)
  - AUTOSAR_CP_TPS_ECUResourceTemplate.pdf (page 60)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 981)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2016)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 437)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_GenericStructure_GeneralTemplateClasses_Identifiable.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    CategoryString,
)
from armodel.models.M2.MSR.AsamHdo.AdminData.admin_data import (
    AdminData,
)
from armodel.models.M2.MSR.Documentation.BlockElements.documentation_block import (
    DocumentationBlock,
)
from armodel.models.M2.MSR.Documentation.TextModel.MultilanguageData.multi_language_overview_paragraph import (
    MultiLanguageOverviewParagraph,
)
from abc import ABC, abstractmethod


class Describable(ARObject, ABC):
    """AUTOSAR Describable."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    admin_data: Optional[AdminData]
    category: Optional[CategoryString]
    desc: Optional[MultiLanguageOverviewParagraph]
    introduction: Optional[DocumentationBlock]
    def __init__(self) -> None:
        """Initialize Describable."""
        super().__init__()
        self.admin_data: Optional[AdminData] = None
        self.category: Optional[CategoryString] = None
        self.desc: Optional[MultiLanguageOverviewParagraph] = None
        self.introduction: Optional[DocumentationBlock] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "Describable":
        """Deserialize XML element to Describable object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized Describable object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse admin_data
        child = ARObject._find_child_element(element, "ADMIN-DATA")
        if child is not None:
            admin_data_value = ARObject._deserialize_by_tag(child, "AdminData")
            obj.admin_data = admin_data_value

        # Parse category
        child = ARObject._find_child_element(element, "CATEGORY")
        if child is not None:
            category_value = child.text
            obj.category = category_value

        # Parse desc
        child = ARObject._find_child_element(element, "DESC")
        if child is not None:
            desc_value = ARObject._deserialize_by_tag(child, "MultiLanguageOverviewParagraph")
            obj.desc = desc_value

        # Parse introduction
        child = ARObject._find_child_element(element, "INTRODUCTION")
        if child is not None:
            introduction_value = ARObject._deserialize_by_tag(child, "DocumentationBlock")
            obj.introduction = introduction_value

        return obj



class DescribableBuilder:
    """Builder for Describable."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: Describable = Describable()

    def build(self) -> Describable:
        """Build and return Describable object.

        Returns:
            Describable instance
        """
        # TODO: Add validation
        return self._obj
