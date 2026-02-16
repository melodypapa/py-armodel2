"""Xref AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

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
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "label1": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=SingleLanguageLongName,
        ),  # label1
        "referrable": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=Referrable,
        ),  # referrable
        "resolution_policy_enum": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=ResolutionPolicyEnum,
        ),  # resolutionPolicyEnum
        "show_content_enum": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=ShowContentEnum,
        ),  # showContentEnum
        "show_resource_alias": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=ShowResourceAliasNameEnum,
        ),  # showResourceAlias
        "show_resource": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=ShowResourceTypeEnum,
        ),  # showResource
        "show_resource_long": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=ShowResourceLongNameEnum,
        ),  # showResourceLong
        "show_resource_number": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=ShowResourceNumberEnum,
        ),  # showResourceNumber
        "show_resource_page": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=ShowResourcePageEnum,
        ),  # showResourcePage
        "show_resource_short": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=ShowResourceShortNameEnum,
        ),  # showResourceShort
        "show_see": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=ShowSeeEnum,
        ),  # showSee
    }

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
