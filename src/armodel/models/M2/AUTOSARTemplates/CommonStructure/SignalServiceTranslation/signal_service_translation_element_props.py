"""SignalServiceTranslationElementProps AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Filter.data_filter import (
    DataFilter,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.data_prototype import (
    DataPrototype,
)


class SignalServiceTranslationElementProps(Identifiable):
    """AUTOSAR SignalServiceTranslationElementProps."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("element", None, False, False, DataPrototype),  # element
        ("filter", None, False, False, DataFilter),  # filter
        ("transmission", None, True, False, None),  # transmission
    ]

    def __init__(self) -> None:
        """Initialize SignalServiceTranslationElementProps."""
        super().__init__()
        self.element: Optional[DataPrototype] = None
        self.filter: Optional[DataFilter] = None
        self.transmission: Optional[Boolean] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert SignalServiceTranslationElementProps to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SignalServiceTranslationElementProps":
        """Create SignalServiceTranslationElementProps from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            SignalServiceTranslationElementProps instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to SignalServiceTranslationElementProps since parent returns ARObject
        return cast("SignalServiceTranslationElementProps", obj)


class SignalServiceTranslationElementPropsBuilder:
    """Builder for SignalServiceTranslationElementProps."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SignalServiceTranslationElementProps = SignalServiceTranslationElementProps()

    def build(self) -> SignalServiceTranslationElementProps:
        """Build and return SignalServiceTranslationElementProps object.

        Returns:
            SignalServiceTranslationElementProps instance
        """
        # TODO: Add validation
        return self._obj
