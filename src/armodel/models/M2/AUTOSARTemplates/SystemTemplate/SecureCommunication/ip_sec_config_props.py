"""IPSecConfigProps AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 572)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_SecureCommunication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SecureCommunication import (
    IPsecDpdActionEnum,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
    String,
    TimeValue,
)


class IPSecConfigProps(ARElement):
    """AUTOSAR IPSecConfigProps."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    ah_cipher_suites: list[String]
    dpd_action: Optional[IPsecDpdActionEnum]
    dpd_delay: Optional[TimeValue]
    esp_cipher_suites: list[String]
    ike_cipher_suite: Optional[String]
    ike_over_time: Optional[TimeValue]
    ike_rand_time: Optional[PositiveInteger]
    ike_reauth_time: Optional[TimeValue]
    ike_rekey_time: Optional[TimeValue]
    sa_over_time: Optional[PositiveInteger]
    sa_rand_time: Optional[TimeValue]
    sa_rekey_time: Optional[TimeValue]
    def __init__(self) -> None:
        """Initialize IPSecConfigProps."""
        super().__init__()
        self.ah_cipher_suites: list[String] = []
        self.dpd_action: Optional[IPsecDpdActionEnum] = None
        self.dpd_delay: Optional[TimeValue] = None
        self.esp_cipher_suites: list[String] = []
        self.ike_cipher_suite: Optional[String] = None
        self.ike_over_time: Optional[TimeValue] = None
        self.ike_rand_time: Optional[PositiveInteger] = None
        self.ike_reauth_time: Optional[TimeValue] = None
        self.ike_rekey_time: Optional[TimeValue] = None
        self.sa_over_time: Optional[PositiveInteger] = None
        self.sa_rand_time: Optional[TimeValue] = None
        self.sa_rekey_time: Optional[TimeValue] = None

    def serialize(self) -> ET.Element:
        """Serialize IPSecConfigProps to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(IPSecConfigProps, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize ah_cipher_suites (list to container "AH-CIPHER-SUITES")
        if self.ah_cipher_suites:
            wrapper = ET.Element("AH-CIPHER-SUITES")
            for item in self.ah_cipher_suites:
                serialized = ARObject._serialize_item(item, "String")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize dpd_action
        if self.dpd_action is not None:
            serialized = ARObject._serialize_item(self.dpd_action, "IPsecDpdActionEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DPD-ACTION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize dpd_delay
        if self.dpd_delay is not None:
            serialized = ARObject._serialize_item(self.dpd_delay, "TimeValue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DPD-DELAY")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize esp_cipher_suites (list to container "ESP-CIPHER-SUITES")
        if self.esp_cipher_suites:
            wrapper = ET.Element("ESP-CIPHER-SUITES")
            for item in self.esp_cipher_suites:
                serialized = ARObject._serialize_item(item, "String")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize ike_cipher_suite
        if self.ike_cipher_suite is not None:
            serialized = ARObject._serialize_item(self.ike_cipher_suite, "String")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("IKE-CIPHER-SUITE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize ike_over_time
        if self.ike_over_time is not None:
            serialized = ARObject._serialize_item(self.ike_over_time, "TimeValue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("IKE-OVER-TIME")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize ike_rand_time
        if self.ike_rand_time is not None:
            serialized = ARObject._serialize_item(self.ike_rand_time, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("IKE-RAND-TIME")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize ike_reauth_time
        if self.ike_reauth_time is not None:
            serialized = ARObject._serialize_item(self.ike_reauth_time, "TimeValue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("IKE-REAUTH-TIME")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize ike_rekey_time
        if self.ike_rekey_time is not None:
            serialized = ARObject._serialize_item(self.ike_rekey_time, "TimeValue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("IKE-REKEY-TIME")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize sa_over_time
        if self.sa_over_time is not None:
            serialized = ARObject._serialize_item(self.sa_over_time, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SA-OVER-TIME")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize sa_rand_time
        if self.sa_rand_time is not None:
            serialized = ARObject._serialize_item(self.sa_rand_time, "TimeValue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SA-RAND-TIME")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize sa_rekey_time
        if self.sa_rekey_time is not None:
            serialized = ARObject._serialize_item(self.sa_rekey_time, "TimeValue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SA-REKEY-TIME")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "IPSecConfigProps":
        """Deserialize XML element to IPSecConfigProps object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized IPSecConfigProps object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(IPSecConfigProps, cls).deserialize(element)

        # Parse ah_cipher_suites (list from container "AH-CIPHER-SUITES")
        obj.ah_cipher_suites = []
        container = ARObject._find_child_element(element, "AH-CIPHER-SUITES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.ah_cipher_suites.append(child_value)

        # Parse dpd_action
        child = ARObject._find_child_element(element, "DPD-ACTION")
        if child is not None:
            dpd_action_value = IPsecDpdActionEnum.deserialize(child)
            obj.dpd_action = dpd_action_value

        # Parse dpd_delay
        child = ARObject._find_child_element(element, "DPD-DELAY")
        if child is not None:
            dpd_delay_value = child.text
            obj.dpd_delay = dpd_delay_value

        # Parse esp_cipher_suites (list from container "ESP-CIPHER-SUITES")
        obj.esp_cipher_suites = []
        container = ARObject._find_child_element(element, "ESP-CIPHER-SUITES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.esp_cipher_suites.append(child_value)

        # Parse ike_cipher_suite
        child = ARObject._find_child_element(element, "IKE-CIPHER-SUITE")
        if child is not None:
            ike_cipher_suite_value = child.text
            obj.ike_cipher_suite = ike_cipher_suite_value

        # Parse ike_over_time
        child = ARObject._find_child_element(element, "IKE-OVER-TIME")
        if child is not None:
            ike_over_time_value = child.text
            obj.ike_over_time = ike_over_time_value

        # Parse ike_rand_time
        child = ARObject._find_child_element(element, "IKE-RAND-TIME")
        if child is not None:
            ike_rand_time_value = child.text
            obj.ike_rand_time = ike_rand_time_value

        # Parse ike_reauth_time
        child = ARObject._find_child_element(element, "IKE-REAUTH-TIME")
        if child is not None:
            ike_reauth_time_value = child.text
            obj.ike_reauth_time = ike_reauth_time_value

        # Parse ike_rekey_time
        child = ARObject._find_child_element(element, "IKE-REKEY-TIME")
        if child is not None:
            ike_rekey_time_value = child.text
            obj.ike_rekey_time = ike_rekey_time_value

        # Parse sa_over_time
        child = ARObject._find_child_element(element, "SA-OVER-TIME")
        if child is not None:
            sa_over_time_value = child.text
            obj.sa_over_time = sa_over_time_value

        # Parse sa_rand_time
        child = ARObject._find_child_element(element, "SA-RAND-TIME")
        if child is not None:
            sa_rand_time_value = child.text
            obj.sa_rand_time = sa_rand_time_value

        # Parse sa_rekey_time
        child = ARObject._find_child_element(element, "SA-REKEY-TIME")
        if child is not None:
            sa_rekey_time_value = child.text
            obj.sa_rekey_time = sa_rekey_time_value

        return obj



class IPSecConfigPropsBuilder:
    """Builder for IPSecConfigProps."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: IPSecConfigProps = IPSecConfigProps()

    def build(self) -> IPSecConfigProps:
        """Build and return IPSecConfigProps object.

        Returns:
            IPSecConfigProps instance
        """
        # TODO: Add validation
        return self._obj
