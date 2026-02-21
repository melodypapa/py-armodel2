"""CryptoEllipticCurveProps AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 564)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_SecureCommunication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)


class CryptoEllipticCurveProps(ARElement):
    """AUTOSAR CryptoEllipticCurveProps."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    named_curve_id: Optional[PositiveInteger]
    def __init__(self) -> None:
        """Initialize CryptoEllipticCurveProps."""
        super().__init__()
        self.named_curve_id: Optional[PositiveInteger] = None

    def serialize(self) -> ET.Element:
        """Serialize CryptoEllipticCurveProps to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(CryptoEllipticCurveProps, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize named_curve_id
        if self.named_curve_id is not None:
            serialized = SerializationHelper.serialize_item(self.named_curve_id, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("NAMED-CURVE-ID")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "CryptoEllipticCurveProps":
        """Deserialize XML element to CryptoEllipticCurveProps object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized CryptoEllipticCurveProps object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(CryptoEllipticCurveProps, cls).deserialize(element)

        # Parse named_curve_id
        child = SerializationHelper.find_child_element(element, "NAMED-CURVE-ID")
        if child is not None:
            named_curve_id_value = child.text
            obj.named_curve_id = named_curve_id_value

        return obj



class CryptoEllipticCurvePropsBuilder:
    """Builder for CryptoEllipticCurveProps."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: CryptoEllipticCurveProps = CryptoEllipticCurveProps()

    def build(self) -> CryptoEllipticCurveProps:
        """Build and return CryptoEllipticCurveProps object.

        Returns:
            CryptoEllipticCurveProps instance
        """
        # TODO: Add validation
        return self._obj
