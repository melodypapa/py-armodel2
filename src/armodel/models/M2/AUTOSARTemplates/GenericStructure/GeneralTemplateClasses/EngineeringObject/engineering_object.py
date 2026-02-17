"""EngineeringObject AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 132)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 160)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_GenericStructure_GeneralTemplateClasses_EngineeringObject.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    NameToken,
    RevisionLabelString,
)


class EngineeringObject(ARObject):
    """AUTOSAR EngineeringObject."""
    """Abstract base class - do not instantiate directly."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "category": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="1",
        ),  # category
        "domain": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # domain
        "revision_label_strings": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
        ),  # revisionLabelStrings
        "short_label": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="1",
        ),  # shortLabel
    }

    def __init__(self) -> None:
        """Initialize EngineeringObject."""
        super().__init__()
        self.category: NameToken = None
        self.domain: Optional[NameToken] = None
        self.revision_label_strings: list[RevisionLabelString] = []
        self.short_label: NameToken = None


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
