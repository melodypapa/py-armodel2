"""BswDataReceptionPolicy AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 104)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_BswModuleTemplate_BswBehavior.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.variable_data_prototype import (
    VariableDataPrototype,
)
from abc import ABC, abstractmethod


class BswDataReceptionPolicy(ARObject, ABC):
    """AUTOSAR BswDataReceptionPolicy."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    received_data_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize BswDataReceptionPolicy."""
        super().__init__()
        self.received_data_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize BswDataReceptionPolicy to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # Serialize received_data_ref
        if self.received_data_ref is not None:
            serialized = SerializationHelper.serialize_item(self.received_data_ref, "VariableDataPrototype")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("RECEIVED-DATA-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "BswDataReceptionPolicy":
        """Deserialize XML element to BswDataReceptionPolicy object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized BswDataReceptionPolicy object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse received_data_ref
        child = SerializationHelper.find_child_element(element, "RECEIVED-DATA-REF")
        if child is not None:
            received_data_ref_value = ARRef.deserialize(child)
            obj.received_data_ref = received_data_ref_value

        return obj



class BswDataReceptionPolicyBuilder:
    """Builder for BswDataReceptionPolicy."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: BswDataReceptionPolicy = BswDataReceptionPolicy()

    def build(self) -> BswDataReceptionPolicy:
        """Build and return BswDataReceptionPolicy object.

        Returns:
            BswDataReceptionPolicy instance
        """
        # TODO: Add validation
        return self._obj
