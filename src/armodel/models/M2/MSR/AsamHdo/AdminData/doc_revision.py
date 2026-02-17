"""DocRevision AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 293)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 85)

JSON Source: docs/json/packages/M2_MSR_AsamHdo_AdminData.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    DateTime,
    NameToken,
    RevisionLabelString,
    String,
)
from armodel.models.M2.MSR.AsamHdo.AdminData.modification import (
    Modification,
)


class DocRevision(ARObject):
    """AUTOSAR DocRevision."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "date": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="1",
        ),  # date
        "issued_by": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # issuedBy
        "modifications": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=Modification,
        ),  # modifications
        "revision_label_string": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # revisionLabelString
        "revision_label_p1": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # revisionLabelP1
        "revision_label_p2": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # revisionLabelP2
        "state": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # state
    }

    def __init__(self) -> None:
        """Initialize DocRevision."""
        super().__init__()
        self.date: DateTime = None
        self.issued_by: Optional[String] = None
        self.modifications: list[Modification] = []
        self.revision_label_string: Optional[RevisionLabelString] = None
        self.revision_label_p1: Optional[RevisionLabelString] = None
        self.revision_label_p2: Optional[RevisionLabelString] = None
        self.state: Optional[NameToken] = None


class DocRevisionBuilder:
    """Builder for DocRevision."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DocRevision = DocRevision()

    def build(self) -> DocRevision:
        """Build and return DocRevision object.

        Returns:
            DocRevision instance
        """
        # TODO: Add validation
        return self._obj
