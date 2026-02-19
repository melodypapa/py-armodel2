"""Xref AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 320)

JSON Source: docs/json/packages/M2_MSR_Documentation_TextModel_InlineTextElements.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.MSR.Documentation.TextModel.InlineAttributeEnums import (
    ResolutionPolicyEnum,
    ShowContentEnum,
    ShowResourceAliasNameEnum,
    ShowResourceLongNameEnum,
    ShowResourceNumberEnum,
    ShowResourcePageEnum,
    ShowResourceShortNameEnum,
    ShowResourceTypeEnum,
    ShowSeeEnum,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.referrable import (
    Referrable,
)
from armodel.models.M2.MSR.Documentation.TextModel.SingleLanguageData.single_language_long_name import (
    SingleLanguageLongName,
)


class Xref(ARObject):
    """AUTOSAR Xref."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    label1: Optional[SingleLanguageLongName]
    referrable_ref: Optional[ARRef]
    resolution_policy_enum: Optional[ResolutionPolicyEnum]
    show_content_enum: Optional[ShowContentEnum]
    show_resource_alias: Optional[ShowResourceAliasNameEnum]
    show_resource: Optional[ShowResourceTypeEnum]
    show_resource_long: Optional[ShowResourceLongNameEnum]
    show_resource_number: Optional[ShowResourceNumberEnum]
    show_resource_page: Optional[ShowResourcePageEnum]
    show_resource_short: Optional[ShowResourceShortNameEnum]
    show_see: Optional[ShowSeeEnum]
    def __init__(self) -> None:
        """Initialize Xref."""
        super().__init__()
        self.label1: Optional[SingleLanguageLongName] = None
        self.referrable_ref: Optional[ARRef] = None
        self.resolution_policy_enum: Optional[ResolutionPolicyEnum] = None
        self.show_content_enum: Optional[ShowContentEnum] = None
        self.show_resource_alias: Optional[ShowResourceAliasNameEnum] = None
        self.show_resource: Optional[ShowResourceTypeEnum] = None
        self.show_resource_long: Optional[ShowResourceLongNameEnum] = None
        self.show_resource_number: Optional[ShowResourceNumberEnum] = None
        self.show_resource_page: Optional[ShowResourcePageEnum] = None
        self.show_resource_short: Optional[ShowResourceShortNameEnum] = None
        self.show_see: Optional[ShowSeeEnum] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "Xref":
        """Deserialize XML element to Xref object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized Xref object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse label1
        child = ARObject._find_child_element(element, "LABEL1")
        if child is not None:
            label1_value = ARObject._deserialize_by_tag(child, "SingleLanguageLongName")
            obj.label1 = label1_value

        # Parse referrable_ref
        child = ARObject._find_child_element(element, "REFERRABLE")
        if child is not None:
            referrable_ref_value = ARObject._deserialize_by_tag(child, "Referrable")
            obj.referrable_ref = referrable_ref_value

        # Parse resolution_policy_enum
        child = ARObject._find_child_element(element, "RESOLUTION-POLICY-ENUM")
        if child is not None:
            resolution_policy_enum_value = ResolutionPolicyEnum.deserialize(child)
            obj.resolution_policy_enum = resolution_policy_enum_value

        # Parse show_content_enum
        child = ARObject._find_child_element(element, "SHOW-CONTENT-ENUM")
        if child is not None:
            show_content_enum_value = ShowContentEnum.deserialize(child)
            obj.show_content_enum = show_content_enum_value

        # Parse show_resource_alias
        child = ARObject._find_child_element(element, "SHOW-RESOURCE-ALIAS")
        if child is not None:
            show_resource_alias_value = ShowResourceAliasNameEnum.deserialize(child)
            obj.show_resource_alias = show_resource_alias_value

        # Parse show_resource
        child = ARObject._find_child_element(element, "SHOW-RESOURCE")
        if child is not None:
            show_resource_value = ShowResourceTypeEnum.deserialize(child)
            obj.show_resource = show_resource_value

        # Parse show_resource_long
        child = ARObject._find_child_element(element, "SHOW-RESOURCE-LONG")
        if child is not None:
            show_resource_long_value = ShowResourceLongNameEnum.deserialize(child)
            obj.show_resource_long = show_resource_long_value

        # Parse show_resource_number
        child = ARObject._find_child_element(element, "SHOW-RESOURCE-NUMBER")
        if child is not None:
            show_resource_number_value = ShowResourceNumberEnum.deserialize(child)
            obj.show_resource_number = show_resource_number_value

        # Parse show_resource_page
        child = ARObject._find_child_element(element, "SHOW-RESOURCE-PAGE")
        if child is not None:
            show_resource_page_value = ShowResourcePageEnum.deserialize(child)
            obj.show_resource_page = show_resource_page_value

        # Parse show_resource_short
        child = ARObject._find_child_element(element, "SHOW-RESOURCE-SHORT")
        if child is not None:
            show_resource_short_value = ShowResourceShortNameEnum.deserialize(child)
            obj.show_resource_short = show_resource_short_value

        # Parse show_see
        child = ARObject._find_child_element(element, "SHOW-SEE")
        if child is not None:
            show_see_value = ShowSeeEnum.deserialize(child)
            obj.show_see = show_see_value

        return obj



class XrefBuilder:
    """Builder for Xref."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: Xref = Xref()

    def build(self) -> Xref:
        """Build and return Xref object.

        Returns:
            Xref instance
        """
        # TODO: Add validation
        return self._obj
