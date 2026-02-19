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
    @classmethod
    def deserialize(cls, element: ET.Element) -> "DocRevision":
        """Deserialize XML element to DocRevision object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DocRevision object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse date
        child = ARObject._find_child_element(element, "DATE")
        if child is not None:
            date_value = child.text
            obj.date = date_value

        # Parse issued_by
        child = ARObject._find_child_element(element, "ISSUED-BY")
        if child is not None:
            issued_by_value = child.text
            obj.issued_by = issued_by_value

        # Parse modifications (list)
        obj.modifications = []
        for child in ARObject._find_all_child_elements(element, "MODIFICATIONS"):
            modifications_value = ARObject._deserialize_by_tag(child, "Modification")
            obj.modifications.append(modifications_value)

        # Parse revision_label_string
        child = ARObject._find_child_element(element, "REVISION-LABEL-STRING")
        if child is not None:
            revision_label_string_value = child.text
            obj.revision_label_string = revision_label_string_value

        # Parse revision_label_p1
        child = ARObject._find_child_element(element, "REVISION-LABEL-P1")
        if child is not None:
            revision_label_p1_value = child.text
            obj.revision_label_p1 = revision_label_p1_value

        # Parse revision_label_p2
        child = ARObject._find_child_element(element, "REVISION-LABEL-P2")
        if child is not None:
            revision_label_p2_value = child.text
            obj.revision_label_p2 = revision_label_p2_value

        # Parse state
        child = ARObject._find_child_element(element, "STATE")
        if child is not None:
            state_value = child.text
            obj.state = state_value

        return obj



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
