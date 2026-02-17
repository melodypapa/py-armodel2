"""Std AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 318)

JSON Source: docs/json/packages/M2_MSR_Documentation_TextModel_InlineTextElements.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.single_language_referrable import (
    SingleLanguageReferrable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    DateTime,
    String,
)


class Std(SingleLanguageReferrable):
    """AUTOSAR Std."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "date": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # date
        "position": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # position
        "state": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # state
        "subtitle": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # subtitle
        "url": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=Any,
        ),  # url
    }

    def __init__(self) -> None:
        """Initialize Std."""
        super().__init__()
        self.date: Optional[DateTime] = None
        self.position: Optional[String] = None
        self.state: Optional[String] = None
        self.subtitle: Optional[String] = None
        self.url: Optional[Any] = None


class StdBuilder:
    """Builder for Std."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: Std = Std()

    def build(self) -> Std:
        """Build and return Std object.

        Returns:
            Std instance
        """
        # TODO: Add validation
        return self._obj
