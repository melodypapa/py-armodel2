"""Xref AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.referrable import (
    Referrable,
)
from armodel.models.M2.MSR.Documentation.TextModel.SingleLanguageData.single_language_long_name import (
    SingleLanguageLongName,
)


class Xref(ARObject):
    """AUTOSAR Xref."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("label1", None, False, False, SingleLanguageLongName),  # label1
        ("referrable", None, False, False, Referrable),  # referrable
        ("resolution_policy_enum", None, False, False, ResolutionPolicyEnum),  # resolutionPolicyEnum
        ("show_content_enum", None, False, False, ShowContentEnum),  # showContentEnum
        ("show_resource_alias", None, False, False, ShowResourceAliasNameEnum),  # showResourceAlias
        ("show_resource", None, False, False, ShowResourceTypeEnum),  # showResource
        ("show_resource_long", None, False, False, ShowResourceLongNameEnum),  # showResourceLong
        ("show_resource_number", None, False, False, ShowResourceNumberEnum),  # showResourceNumber
        ("show_resource_page", None, False, False, ShowResourcePageEnum),  # showResourcePage
        ("show_resource_short", None, False, False, ShowResourceShortNameEnum),  # showResourceShort
        ("show_see", None, False, False, ShowSeeEnum),  # showSee
    ]

    def __init__(self) -> None:
        """Initialize Xref."""
        super().__init__()
        self.label1: Optional[SingleLanguageLongName] = None
        self.referrable: Optional[Referrable] = None
        self.resolution_policy_enum: Optional[ResolutionPolicyEnum] = None
        self.show_content_enum: Optional[ShowContentEnum] = None
        self.show_resource_alias: Optional[ShowResourceAliasNameEnum] = None
        self.show_resource: Optional[ShowResourceTypeEnum] = None
        self.show_resource_long: Optional[ShowResourceLongNameEnum] = None
        self.show_resource_number: Optional[ShowResourceNumberEnum] = None
        self.show_resource_page: Optional[ShowResourcePageEnum] = None
        self.show_resource_short: Optional[ShowResourceShortNameEnum] = None
        self.show_see: Optional[ShowSeeEnum] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert Xref to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "Xref":
        """Create Xref from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            Xref instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to Xref since parent returns ARObject
        return cast("Xref", obj)


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
