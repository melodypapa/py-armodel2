"""SdgForeignReference AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 102)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_GenericStructure_GeneralTemplateClasses_SpecialDataDef.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.SpecialDataDef.sdg_abstract_foreign_reference import (
    SdgAbstractForeignReference,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject


class SdgForeignReference(SdgAbstractForeignReference):
    """AUTOSAR SdgForeignReference."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    def __init__(self) -> None:
        """Initialize SdgForeignReference."""
        super().__init__()

    def serialize(self) -> ET.Element:
        """Serialize SdgForeignReference to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(SdgForeignReference, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SdgForeignReference":
        """Deserialize XML element to SdgForeignReference object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SdgForeignReference object
        """
        # Delegate to parent class to handle inherited attributes
        return super(SdgForeignReference, cls).deserialize(element)



class SdgForeignReferenceBuilder:
    """Builder for SdgForeignReference."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SdgForeignReference = SdgForeignReference()

    def build(self) -> SdgForeignReference:
        """Build and return SdgForeignReference object.

        Returns:
            SdgForeignReference instance
        """
        # TODO: Add validation
        return self._obj
