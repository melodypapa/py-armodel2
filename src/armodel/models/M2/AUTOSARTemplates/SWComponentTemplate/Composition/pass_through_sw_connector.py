"""PassThroughSwConnector AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 83)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2043)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_Composition.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Composition.sw_connector import (
    SwConnector,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.abstract_provided_port_prototype import (
    AbstractProvidedPortPrototype,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.abstract_required_port_prototype import (
    AbstractRequiredPortPrototype,
)


class PassThroughSwConnector(SwConnector):
    """AUTOSAR PassThroughSwConnector."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    provided_outer_ref: Optional[ARRef]
    required_outer_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize PassThroughSwConnector."""
        super().__init__()
        self.provided_outer_ref: Optional[ARRef] = None
        self.required_outer_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize PassThroughSwConnector to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(PassThroughSwConnector, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize provided_outer_ref
        if self.provided_outer_ref is not None:
            serialized = ARObject._serialize_item(self.provided_outer_ref, "AbstractProvidedPortPrototype")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PROVIDED-OUTER-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize required_outer_ref
        if self.required_outer_ref is not None:
            serialized = ARObject._serialize_item(self.required_outer_ref, "AbstractRequiredPortPrototype")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("REQUIRED-OUTER-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "PassThroughSwConnector":
        """Deserialize XML element to PassThroughSwConnector object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized PassThroughSwConnector object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(PassThroughSwConnector, cls).deserialize(element)

        # Parse provided_outer_ref
        child = ARObject._find_child_element(element, "PROVIDED-OUTER-REF")
        if child is not None:
            provided_outer_ref_value = ARRef.deserialize(child)
            obj.provided_outer_ref = provided_outer_ref_value

        # Parse required_outer_ref
        child = ARObject._find_child_element(element, "REQUIRED-OUTER-REF")
        if child is not None:
            required_outer_ref_value = ARRef.deserialize(child)
            obj.required_outer_ref = required_outer_ref_value

        return obj



class PassThroughSwConnectorBuilder:
    """Builder for PassThroughSwConnector."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: PassThroughSwConnector = PassThroughSwConnector()

    def build(self) -> PassThroughSwConnector:
        """Build and return PassThroughSwConnector object.

        Returns:
            PassThroughSwConnector instance
        """
        # TODO: Add validation
        return self._obj
