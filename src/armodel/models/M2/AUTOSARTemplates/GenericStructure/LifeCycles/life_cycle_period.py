"""LifeCyclePeriod AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 392)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_GenericStructure_LifeCycles.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    DateTime,
    RevisionLabelString,
)


class LifeCyclePeriod(ARObject):
    """AUTOSAR LifeCyclePeriod."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    ar_release: Optional[RevisionLabelString]
    date: Optional[DateTime]
    product_release: Optional[RevisionLabelString]
    def __init__(self) -> None:
        """Initialize LifeCyclePeriod."""
        super().__init__()
        self.ar_release: Optional[RevisionLabelString] = None
        self.date: Optional[DateTime] = None
        self.product_release: Optional[RevisionLabelString] = None

    def serialize(self) -> ET.Element:
        """Serialize LifeCyclePeriod to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # Serialize ar_release
        if self.ar_release is not None:
            serialized = ARObject._serialize_item(self.ar_release, "RevisionLabelString")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("AR-RELEASE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize date
        if self.date is not None:
            serialized = ARObject._serialize_item(self.date, "DateTime")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DATE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize product_release
        if self.product_release is not None:
            serialized = ARObject._serialize_item(self.product_release, "RevisionLabelString")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PRODUCT-RELEASE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "LifeCyclePeriod":
        """Deserialize XML element to LifeCyclePeriod object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized LifeCyclePeriod object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse ar_release
        child = ARObject._find_child_element(element, "AR-RELEASE")
        if child is not None:
            ar_release_value = child.text
            obj.ar_release = ar_release_value

        # Parse date
        child = ARObject._find_child_element(element, "DATE")
        if child is not None:
            date_value = child.text
            obj.date = date_value

        # Parse product_release
        child = ARObject._find_child_element(element, "PRODUCT-RELEASE")
        if child is not None:
            product_release_value = child.text
            obj.product_release = product_release_value

        return obj



class LifeCyclePeriodBuilder:
    """Builder for LifeCyclePeriod."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: LifeCyclePeriod = LifeCyclePeriod()

    def build(self) -> LifeCyclePeriod:
        """Build and return LifeCyclePeriod object.

        Returns:
            LifeCyclePeriod instance
        """
        # TODO: Add validation
        return self._obj
