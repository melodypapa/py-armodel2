"""DocRevision AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 293)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 85)

JSON Source: docs/json/packages/M2_MSR_AsamHdo_AdminData.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

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

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    date: DateTime
    issued_by: Optional[String]
    modifications: list[Modification]
    revision_label_string: Optional[RevisionLabelString]
    revision_label_p1: Optional[RevisionLabelString]
    revision_label_p2: Optional[RevisionLabelString]
    state: Optional[NameToken]
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
